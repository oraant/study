from django.contrib import admin
from .models import *

# Register your models here.

#class G2T(admin.InlineModelAdmin):
#class G2T(admin.TabularInline):
#class G2T(admin.StackedInline):
    #model = Group.teachers.through
    #filter_horizontal = ['teacher']
    #fields = ('name', 'sex')

#class G2S(admin.TabularInline):
    #model = Student
    #list_display = ['id', 'name', 'sex']

# ----------

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sex']
    list_filter = ['group']
    #filter_horizontal = ['group']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sex']
    pass

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sex']
    list_filter = ['teachers']
    filter_horizontal = ['teachers']
