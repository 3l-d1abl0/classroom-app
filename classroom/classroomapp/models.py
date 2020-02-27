from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=30)
    doj= models.DateField()
    subjects = models.ManyToManyField("Subject")
    salary = models.FloatField()
    web_lecture = models.BooleanField(default=False) 

    def __str__(self):
        return self.teacher_name


class Subject(models.Model):
    subject_name = models.CharField(max_length=30)
    chapters = models.ManyToManyField("Chapter")
    total_duration = models.IntegerField()
    duration_per_class = models.IntegerField(default=30,validators=[MaxValueValidator(120), MinValueValidator(30)])

    def __str__(self):
        return self.subject_name


class Chapter(models.Model):
    chapter_name = models.CharField(max_length=30)

    def __str__(self):
        return self.chapter_name


class Student(models.Model):
    student_name = models.CharField(max_length=30)
    doj = models.DateField()
    standard = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    roll_no = models.IntegerField()
    rank = models.IntegerField()
    point_of_contact = models.ManyToManyField("PointOfContact")

    def __str__(self):
        return self.student_name


class PointOfContact(models.Model):
    full_name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=10)
    relation = models.CharField(max_length=30)

    def __str__(self):
        return self.full_name

class Classroom(models.Model):
    seating_capacity = models.IntegerField(default=15, validators=[MinValueValidator(15)])
    web_lecture_support = models.BooleanField(default=False)
    shape = models.ForeignKey("ClassroomShape", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}".format(self.shape)


class ClassroomShape(models.Model):
    type = models.CharField(max_length=15)
    count = models.IntegerField(default=1)

    def __str__(self):
        return "{}".format(self.type)

class Class(models.Model):
    room = models.ForeignKey("Classroom", on_delete=models.CASCADE)
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE)
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)
    students = models.ManyToManyField("Student")

    def __str__(self):
        return "Room {} occupied by {} for {}".format(self.room.shape, self.teacher.teacher_name, self.subject.subject_name)