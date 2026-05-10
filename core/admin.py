from django.contrib import admin
from .models import Assistant, Student, Course

@admin.register(Assistant)
class AssistantAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'code') 
    readonly_fields = ('code',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'code')
    readonly_fields = ('code',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    readonly_fields = ('code',)