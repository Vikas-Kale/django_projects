from django.db import models

# Create your models here.

class Contact(models.Model):
    lname=models.CharField(max_length=122)
    fname=models.CharField(max_length=122)
    email=models.EmailField()
    comment=models.TextField()
    def __str__(self):
        return self.fname
