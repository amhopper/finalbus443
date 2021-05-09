from django.db import models

# Create your models here.
class Studentdetails(models.Model):
    studentid = models.IntegerField()
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    major = models.CharField(max_length=500)
    year = models.CharField(max_length=500)
    gpa = models.IntegerField()

class Coursedetails(models.Model):
    courseid = models.IntegerField()
    coursetitle = models.CharField(max_length=500)
    coursename = models.CharField(max_length=500)
    coursesectioncode = models.IntegerField()
    coursedepartment = models.CharField(max_length=500)
    instructorfull = models.CharField(max_length=500)

class Courseenrollment(models.Model):
    studentid = models.IntegerField()
    coursename = models.CharField(max_length=500)
