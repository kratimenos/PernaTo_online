from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import random

def generateCode():
    return str(random.randint(100000, 999999))


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    code = models.CharField(validators=[RegexValidator(r'^\d{6}$')], max_length=6, default=generateCode, editable=False, unique=True)
    
    is_student = models.BooleanField(default=True)
    is_assistant = models.BooleanField(default=False)
    is_active_mentor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.surname} ({self.user.username})"


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(validators=[RegexValidator(r'^\d{6}$')], max_length=6, default=generateCode, editable=False, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='courses', null=True, blank=True)
    
    assistants = models.ManyToManyField(UserProfile, related_name='courses_teaching', blank=True)
    students = models.ManyToManyField(UserProfile, related_name='courses_enrolled', blank=True)

    def __str__(self):
        return self.name
    


# Signals to automatically create and save UserProfile when a User is created or saved
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()