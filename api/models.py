from django.db import models

# Create your models here.


class Project(models.Model):
    '''
  Project models
  '''
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=250)
    description = models.CharField(max_length=255, blank=True)
    codeUrl = models.URLField()
    liveDemoUrl = models.URLField()
    previewImageUrl = models.ImageField(null=True, blank=True, upload_to='images/')
    heroImageUrl = models.ImageField(null=True, blank=True, upload_to='images/')
    body = models.CharField(max_length=255, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
