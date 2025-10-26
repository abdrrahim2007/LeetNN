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
    #  - Optionally normalizes/slugifies ids (useful if you want to guarantee valid HTML id tokens).

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
                # Prefer using path when available (fast, native file access)
                if hasattr(self.file, 'path') and self.file.path:
                    with open(self.file.path, 'r', encoding='utf-8') as fh:
                        content = fh.read()
                else:
                    # Fallback to Django Storage API (works for InMemoryUploadedFile, S3, etc.)
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
