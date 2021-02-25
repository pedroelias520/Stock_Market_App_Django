from django.db import models

class Operacao (models.Model):
    qtd = models.IntegerField()
    price = models.FloatField()
    tax = models.FloatField()
    type_operation = models.CharField(max_length=2)
    date = models.DateField()

class User(models.Model):
    email = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    