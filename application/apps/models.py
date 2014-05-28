from django.db import models

class Applicant(models.Model):
    lastname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    essay = models.FileField(upload_to='essays')

class Recommender(models.Model):
    applicant = models.ForeignKey(Applicant)
    lastname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    letter = models.FileField(upload_to='letters')
