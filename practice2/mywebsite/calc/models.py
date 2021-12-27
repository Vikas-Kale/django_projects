from django.db import models

# Create your models here.

class Contact(models.Model):
    fname = models.CharField(max_length=122)
    lname = models.CharField(max_length=122)
    email = models.EmailField()
    comment = models.TextField()
    def __str__(self):
        return self.name