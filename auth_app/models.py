from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    role = models.CharField(choices=[('admin', 'Admin'), ('agency', 'Agency'), ('client', 'Client')], max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    refresh_token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = "users"
        ordering = ["-created_at"]

    