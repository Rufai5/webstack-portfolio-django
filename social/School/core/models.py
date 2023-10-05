from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Student(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    courses = models.ManyToManyField("Course", blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Student"

class Course(models.Model):
    name = models.TextField()
    year = models.IntegerField()
    instructor = models.ForeignKey("Student", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ("name", "year", )

class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.course}"
