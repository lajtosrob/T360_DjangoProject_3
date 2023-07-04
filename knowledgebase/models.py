from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name   

class Knowledge(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name