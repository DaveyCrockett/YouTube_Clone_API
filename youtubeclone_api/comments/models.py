from django.db import models

# Create your models here.


class Comment(models.Model):
    video_id = models.CharField(max_length=100)
    comment = models.CharField(max_length=300)
    comment_replys = models.CharField(max_length=300)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    create_date = models.DateField()

    def __str__(self):
        return self.video_id
