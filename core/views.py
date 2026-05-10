from django.shortcuts import render
from .models import Assistant, Course

def home_view(request):
    assistants = Assistant.objects.all()
    return render(request, 'home.html', {'assistants': assistants})

def courses_view(request):
    courses = Course.objects.all()
    return render(request, 'courses.html')

def exercises_view(request):
    return render(request, 'exercises.html')

def assistants_view(request):
    assistants = Assistant.objects.all()
    return render(request, 'assistants.html', {'assistants': assistants})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def become_assistant_view(request):
    return render(request, 'become_assistant.html')