from django.db import models

# Create your models here.
class Post_Customer(models.Model):
    Birth = models.BooleanField(default = False)
    Child = models.BooleanField(default = False)
    Educ = models.BooleanField(default = False)
    Inco = models.BooleanField(default = False)
    Marr = models.BooleanField(default = False)
    Rece = models.BooleanField(default = False)
    Teen = models.BooleanField(default = False)
    
class Post_Cunsumption(models.Model):
    Gold = models.BooleanField(default = False)
    Fruit = models.BooleanField(default = False)
    Meat = models.BooleanField(default = False)
    Fish = models.BooleanField(default = False)
    Snack = models.BooleanField(default = False)
    Wine = models.BooleanField(default = False)
    Teen = models.BooleanField(default = False)
    