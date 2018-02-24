from django.shortcuts import render
from django.views.generic import ListView
from personal.models import Project


def index(request):
    return render(request, 'personal/index.html')


def about(request):
    return render(request, 'personal/aboutme.html')


class ProjectView(ListView):
    queryset = Project.objects.all().order_by('position')
    template_name = 'personal/projects.html'


def contact(request):
    return render(request, 'personal/contact.html')


def resume(request):
    return render(request, 'personal/resume.html')

