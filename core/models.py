from django.db import models
from django.core.validators import RegexValidator


# Abstract model for Teacher ans Student
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    code = models.CharField(validators=[RegexValidator(r'^\d{6}$')], max_length=6, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Teacher(Person):
    pass


class Student(Person):
    pass


class Course(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(validators=[RegexValidator(r'^\d{6}$')], max_length=6, unique=True)
    description = models.TextField()
    teachers = models.ManyToManyField(Teacher, related_name='courses', blank=True)
    students = models.ManyToManyField(Student, related_name='courses', blank=True)

    def __str__(self):
        return self.name
    