from django.contrib import admin

#Register your models here.

from core.models import Student, Course, Grade

@admin.register(Student)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass
