from django.shortcuts import render, redirect
from .models import UserProfile, Course, Category

def home_view(request):
    assistants = UserProfile.objects.filter(is_assistant=True, is_active_mentor=True)
    return render(request, 'home.html', {'assistants': assistants})

def assistants_view(request):
    assistants = UserProfile.objects.filter(is_assistant=True, is_active_mentor=True)
    return render(request, 'assistants.html', {'assistants': assistants})

def courses_view(request):
    categories = Category.objects.prefetch_related('courses').all()
    return render(request, 'courses.html', {'categories': categories})

def exercises_view(request):
    return render(request, 'exercises.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def become_assistant_view(request):
    return render(request, 'become_assistant.html')

def search_view(request):
    query = request.GET.get('q')
    if query:
        courses = Course.objects.filter(name__icontains=query)
    else:
        courses = Course.objects.all()
    return render(request, 'search.html', {'courses': courses})