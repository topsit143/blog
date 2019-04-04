from django.db import models

# Create your models here.
class Job(models.Module):
    image=models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=200)
