
from django.urls import path
from . import views
urlpatterns = [
path('',views.home,name='home'),
path('departments',views.department_list,name='departments'),
path('departments/<slug:dep>/<slug:course_slug>/', views.course_view, name='course_view'),
path('departments/<slug:dep>/<slug:course_slug>/<slug:chapter_slug>/', views.chapter_view, name='chapter_view'),


]
