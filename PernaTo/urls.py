from django.contrib import admin
from django.urls import path, include
from core.views import home_view, courses_view, assistants_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'), 
    path('courses/', courses_view, name='courses'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('assistants/', include('core.urls')),
]