from django.db import models
from petstagram_app.photos.models import Photo


class Comment(models.Model):
    class Meta:
        indexes = [models.Index(fields=['date_time_of_publication'])]
        ordering = ['-date_time_of_publication']

    comment_text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)