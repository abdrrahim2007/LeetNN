from django.shortcuts import render, get_object_or_404,redirect
from .models import Department, Course, Chapter

def home(request):
    return render(request,"base/index.html",{})
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'base/departments.html', {'departments': departments})

def course_view(request,dep,course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    chapters = course.chapters.all().order_by('id')  # or by another field like 'order' if you have one
    
    # If course has at least one chapter → redirect to first chapter
    if chapters.exists():
        first_chapter = chapters.first()
        return redirect('chapter_view', dep=dep, course_slug=course_slug, chapter_slug=first_chapter.slug)

    return render(request,'base/course.html',{'course':course,'chapters':chapters})


def chapter_view(request,dep,course_slug,chapter_slug):
    course = get_object_or_404(Course, slug=course_slug)
    chapter_c = get_object_or_404(Chapter, slug=chapter_slug)
    chapters = course.chapters.all()
    return render(request,'base/course.html',{'course':course,'chapters':chapters,'chapter_c':chapter_c})
