from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_id = models.CharField(max_length=32)
    creator_nickname = models.CharField(max_length=64)
    blog_content = models.CharField(max_length=1024)
    creator_id = models.CharField(max_length=64)
    created_time = models.CharField(max_length=128)

    def __unicode__(self):
        return self.creator_nickname