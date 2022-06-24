from django.db import models

# Create your models here.


class Project(models.Model):
    '''
  Project models
  '''
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    codeUrl = models.URLField()
    liveDemoUrl = models.URLField()
    previewImageUrl = models.URLField()
    heroImageUrl = models.URLField()
    body = models.CharField(max_length=255, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
