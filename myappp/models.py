from django.db import models

class Member(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phone =models.IntegerField(null=True)
    joined_date =models.DateField(null=True)
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
# Create your models here.

class GeeksModel(models.Model):
    title=models.CharField(max_length=200)
    description =models.TextField()
    last_modified=models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.title