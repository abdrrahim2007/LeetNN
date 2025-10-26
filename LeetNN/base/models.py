from django.db import models
from django.utils.text import slugify
import re
import logging

logger = logging.getLogger(__name__)


# ---------- Utility Function ----------
def generate_unique_slug(model_instance, title, slug_field_name='slug'):
    slug = slugify(title)
    ModelClass = model_instance.__class__
    unique_slug = slug
    num = 1
    while ModelClass.objects.filter(**{slug_field_name: unique_slug}).exists():
        unique_slug = f"{slug}-{num}"
        num += 1
    return unique_slug


# ---------- Department ----------
class Department(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ---------- Course ----------
class Course(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ---------- Chapter ----------
class Chapter(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='chapters'
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, max_length=200)

    # Upload field for markdown/HTML content
    file = models.FileField(upload_to='chapters/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # ------------------ Section ID Extraction ------------------
    # Two helpers are provided:
    #  - section_ids (property): returns a list of unique section ids in document order.
    #  - get_section_ids(normalize=False): same as above but allows optional normalization
    #
    # Behaviour & improvements:
    #  - Works with local filesystem or Django storage backends (reads from file object when no .path).
    #  - Uses BeautifulSoup (if installed) for robust HTML parsing. Falls back to a safe regex when bs4 isn't available.
    #  - Accepts both single and double quoted id attributes, ignores empty ids, and preserves document order.
  

    @property
    def section_ids(self):
        """Return a list of unique section ids in the order they appear in the file."""
        return self.get_section_ids()

    def get_section_ids(self, normalize: bool = False):
        """
        Extract <section> element ids from the uploaded file and return them as a list.

        Args:
            normalize: If True, slugify each id (makes them safe for use as HTML ids).

        Returns:
            List[str]: unique section ids in document order.
        """
        if not self.file:
            return []

        try:
            # Read file contents regardless of storage backend
            try:
                if hasattr(self.file, 'path') and self.file.path:
                    with open(self.file.path, 'r', encoding='utf-8') as fh:
                        content = fh.read()
                else:
                    self.file.open('r')
                    raw = self.file.read()
                    # raw can be bytes or str
                    content = raw.decode('utf-8', errors='ignore') if isinstance(raw, (bytes, bytearray)) else str(raw)
            except Exception:
                # As a last fallback, try reading without specifying mode
                try:
                    raw = self.file.read()
                    content = raw.decode('utf-8', errors='ignore') if isinstance(raw, (bytes, bytearray)) else str(raw)
                except Exception as e:
                    logger.exception("Failed to read chapter file: %s", e)
                    return []

            # Try using BeautifulSoup if available for robust parsing
            try:
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(content, 'html.parser')
                found_ids = [tag.get('id') for tag in soup.find_all('section') if tag.get('id')]
            except Exception:
                pattern = re.compile(r'<section\b[^>]*\bid\s*=\s*["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)
                found_ids = pattern.findall(content)

            # Clean and preserve order + uniqueness
            cleaned = []
            for raw_id in found_ids:
                if not raw_id:
                    continue
                token = raw_id.strip().split()[0]  
                if normalize:
                    token = slugify(token)
                cleaned.append(token)

            seen = set()
            unique_ids = []
            for idv in cleaned:
                if idv not in seen:
                    seen.add(idv)
                    unique_ids.append(idv)

            return unique_ids

        except Exception as e:
            logger.exception("Error extracting section ids: %s", e)
            return []







from django.db import models
from django.utils.text import slugify
import os
from PIL import Image,ImageDraw
import zipfile
from io import BytesIO
from pdf2image import convert_from_path
from django.conf import settings

# ---------- Library Model ----------
class Library(models.Model):
    FORMAT_CHOICES = [
        ("PDF", "PDF"),
        ("EPUB", "EPUB"),
        ("MOBI", "MOBI"),
        ("RMD", "RMD"),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=True)
    file = models.FileField(upload_to="books/")

    def __str__(self):
        return self.title

    @property
    def thumbnail_url(self):
        if self.thumbnail:
            return self.thumbnail.url
        # fallback icon path in static
        return f"/static/icons/{self.format.lower()}.png"

    @property
    def file_url(self):
        return self.file.url if self.file else ""

    # ---------- Thumbnail Generation ----------
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save first to have file.path

        if self.thumbnail:  # already has thumbnail
            return

        # Define thumbnail path
        thumb_path = os.path.join(settings.MEDIA_ROOT, "thumbnails", f"{slugify(self.title)}_thumb.jpg")
        os.makedirs(os.path.dirname(thumb_path), exist_ok=True)

        try:
            if self.format.upper() == "PDF":
                # Generate thumbnail from first page of PDF
                images = convert_from_path(self.file.path, first_page=1, last_page=1)
                if images:
                    images[0].save(thumb_path, "JPEG")
                    self.thumbnail.name = os.path.relpath(thumb_path, settings.MEDIA_ROOT)
                    super().save(update_fields=["thumbnail"])

            elif self.format.upper() == "EPUB":
                # Extract cover from EPUB if exists
                with zipfile.ZipFile(self.file.path, 'r') as epub:
                    for f in epub.namelist():
                        if 'cover' in f.lower() and f.lower().endswith(('.jpg', '.jpeg', '.png')):
                            cover_data = epub.read(f)
                            image = Image.open(BytesIO(cover_data))
                            image.thumbnail((300, 400))
                            image.save(thumb_path)
                            self.thumbnail.name = os.path.relpath(thumb_path, settings.MEDIA_ROOT)
                            super().save(update_fields=["thumbnail"])
                            break

            elif self.format.upper() == "RMD":
                # Generate a simple text preview thumbnail
                with open(self.file.path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                title_line = next((l.strip() for l in lines if l.strip()), "RMD Document")
                img = Image.new("RGB", (300, 400), color=(245, 245, 245))
                draw = ImageDraw.Draw(img)
                from PIL import ImageFont
                font = ImageFont.load_default()
                draw.text((20, 180), title_line, fill="black", font=font)
                img.save(thumb_path)
                self.thumbnail.name = os.path.relpath(thumb_path, settings.MEDIA_ROOT)
                super().save(update_fields=["thumbnail"])

            # MOBI or others → fallback icon (do nothing, frontend shows /static/icons/mobi.png)
        except Exception as e:
            import logging
            logging.exception(f"Thumbnail generation failed for {self.title}: {e}")
