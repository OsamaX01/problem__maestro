from django.db import models

from users.models import CustomUser
from problem.models import Problem

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="my_courses", limit_choices_to={'role': 'instructor'})
    students = models.ManyToManyField(CustomUser, blank=True, related_name="courses", limit_choices_to={'role': 'student'})
    problems = models.ManyToManyField(Problem, blank=True, related_name="courses")

    def __str__(self):
        return f"{self.name} course"