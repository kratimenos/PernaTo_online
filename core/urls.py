from django.urls import path
from . import views 

urlpatterns = [
    # ... άλλες διαδρομές ...
    path('assistants/', views.assistants_view, name='assistants'), # ΠΡΟΣΟΧΗ στο name='assistants'
    path('about/', views.about_view, name='about'),
    path('courses/', views.courses_view, name='courses'),
    path('exercises/', views.exercises_view, name='exercises'),
    path('contact/', views.contact_view, name='contact'),
    path('search/', views.search_view, name='search'),
    path('become-assistant/', views.become_assistant_view, name='become_assistant'),
]