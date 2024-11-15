from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=20)
    content = models.TextField()
    depart = models.CharField(max_length=30)
    add_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    upp_date = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
