from django.db import models


# Create your models here.
# Id card database table.
class IDCard(models.Model):
    image = models.ImageField(upload_to="images/id-card/")
    id_card_number = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    dob = models.CharField(max_length=10, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    hometown = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)


# Student card database table.
class Student_Card(models.Model):
    image = models.ImageField(upload_to="images/student-card/")
    student_card_number = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    falculty = models.CharField(max_length=255, blank=True, null=True)
    course = models.CharField(max_length=255, blank=True, null=True)
