
from statistics import mode
from django.db import models

# Create your models here.
class CourtCase(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    entity = models.TextField(default="",blank=True)

    def __str__(self) -> str:
        return str(self.name)



class File(models.Model):
    description = models.CharField(max_length=255)
    document  = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now=True)