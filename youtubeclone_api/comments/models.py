from django.db import models

# Create your models here.


class Comment(models.Model):
    comment = models.CharField(max_length=300)
    commentId = models.IntegerField(default=None)
    videoId = models.CharField(max_length=300)

    def __str__(self):
        return self.comment
