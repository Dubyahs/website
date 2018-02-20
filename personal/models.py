from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=140)
    position = models.IntegerField()
    description = models.TextField()
    img = models.FileField(upload_to='personal/')
    link = models.TextField()

    def __str__(self):
        return self.title
