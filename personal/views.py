from django.shortcuts import render


def index(request):
    return render(request, 'personal/index.html')


def about(request):
    return render(request, 'personal/aboutme.html')


def contact(request):
    return render(request, 'personal/contact.html')


def resume(request):
    return render(request, 'personal/resume.html')

