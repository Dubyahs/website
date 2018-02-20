from django.urls import path
from . import views
from personal.models import Project
from django.views.generic import ListView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.about, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', ListView.as_view(queryset=Project.objects.all().order_by('position'),
                                       template_name="personal/projects.html")),
    path('contact/', views.contact, name='contact'),
    path('resume/', views.resume, name='resume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)