from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=140)
    position = models.PositiveIntegerField(unique=True, null=True)
    description = models.TextField(blank=True)
    img = models.FileField(upload_to='personal/', blank=True)
    link = models.TextField(blank=True)

    def __str__(self):
        return self.title
