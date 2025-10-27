from django.shortcuts import render, get_object_or_404,redirect
from .models import Department, Course, Chapter




def home(request):
    return render(request,"base/index.html",{})
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'base/departments.html', {'departments': departments})

def course_view(request,dep,course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    chapters = course.chapters.all().order_by('id')  
    if chapters.exists():
        first_chapter = chapters.first()
        return redirect('chapter_view', dep=dep, course_slug=course_slug, chapter_slug=first_chapter.slug)

    return render(request,'base/course.html',{'course':course,'chapters':chapters})


def chapter_view(request,dep,course_slug,chapter_slug):
    course = get_object_or_404(Course, slug=course_slug)
    chapter_c = get_object_or_404(Chapter, slug=chapter_slug)
    chapters = course.chapters.all()
    return render(request,'base/course.html',{'course':course,'chapters':chapters,'chapter_c':chapter_c})


def library_view(request):
    return render(request,"base/library.html")


from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from .models import Library
from .serializers import LibrarySerializer



from rest_framework.pagination import PageNumberPagination

class LibraryPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'

class LibraryListView(generics.ListAPIView):
    queryset = Library.objects.all().order_by("id")
    serializer_class = LibrarySerializer
    search_fields = ["title", "author"]
    filterset_fields = ["category", "format", "year"]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    pagination_class = LibraryPagination



@api_view(["GET"])
def Library_filters(request):
    categories = list(Library.objects.exclude(category="").values_list("category", flat=True).distinct())
    years = list(Library.objects.exclude(year=None).values_list("year", flat=True).distinct())
    return Response({"categories": categories, "years": years})




@api_view(["GET"])
def Library_download(request, pk):
    try:
        library = Library.objects.get(pk=pk)
        return Response({"file_url": library.file.url})
    except library.DoesNotExist:
        return Response({"error": "Element not found"}, status=404)



