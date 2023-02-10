from django.db import models

# Create your models here.


class Publisher(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
