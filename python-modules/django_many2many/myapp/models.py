#rom __future__ import unicode_literals

from django.db import models

# Create your models here.
class Teacher(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    # groups = models.ManyToManyField(Group, blank=True, null=True)

class Group(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    teachers = models.ManyToManyField(Teacher, blank=True, null=True)

class Student(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    group = models.ForeignKey(Group, blank=True, null=True)
