from django.db import models 
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

class TeachingContent(models.Model):
    topic = models.CharField(max_length=500,)
    content = RichTextUploadingField()

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('learn:content-detail', kwargs={'pk':self.pk})


