from django.contrib import admin
from .models import UserProfile, Category, Course

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'is_assistant', 'is_active_mentor', 'code')
    list_filter = ('is_assistant', 'is_active_mentor')
    search_fields = ('name', 'surname', 'user__username')
    readonly_fields = ('code',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'code')
    list_filter = ('category',)
    search_fields = ('name',)
    readonly_fields = ('code',)

admin.site.register(Category)