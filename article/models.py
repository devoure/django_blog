from django.db import models
from time import time
from django_test import settings

def get_upload_file_name (instance, filename):
    return settings.UPLOAD_FILE_PATTERN % (str(time()).replace('.','_'), filename)

# Create your models here.
# Create your class Article that inherits from base class Model
class Article(models.Model):
    title = models.CharField(max_length = 200)
    body =models.TextField()
    pub_date =models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    thumbnail=models.FileField(upload_to=get_upload_file_name, default = 'SOME STRING')

    #this will give a name title to each object instance
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return "/articles/get/%i/"% self.id

    def get_thumbnail (self):
        thumb = str(self.thumbnail)
        if not settings.DEBUG:
            thumb = thumb.replace('assets/', '')
        return thumb


class Comment(models.Model):
    name = models.CharField(max_length= 200)
    body = models.TextField()
    pub_date = models.DateTimeField('Date Published')
    article = models.ForeignKey(Article,
                                related_name="commented_post",
                                on_delete = models.DO_NOTHING)

