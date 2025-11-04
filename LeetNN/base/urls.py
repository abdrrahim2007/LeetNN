
from django.urls import path
from . import views




from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
path('',views.home,name='home'),
path('categories/',views.category_list,name='categories'),
path('library/',views.library_view,name='library'),
path('categories/<slug:cat>/<slug:course_slug>/', views.course_view_new, name='course_view_new'),
path('categories/<slug:cat>/<slug:course_slug>/<slug:chapter_slug>/', views.chapter_view, name='chapter_view'),
path("api/library/", views.LibraryListView.as_view(), name="Library_list"),
path("api/library/filters/", views.Library_filters, name="Library_filters"),
path("api/library/<int:pk>/download/", views.Library_download, name="Library_download"),

]
