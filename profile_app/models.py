from django.db import models

role = (
    ('admin', 'admin'),
    ('agency', 'agency'),
    ('client', 'client')
)

# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    profilePicture = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=role)