from django.db import models
from ckeditor.fields import RichTextField
from backend.models import Post


class Subscriber(models.Model):
    email = models.EmailField(max_length=255)
    n_phone = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} with email {self.email}"


class Comment(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nama anonim kamu : ")
    content = RichTextField(config_name='comment', verbose_name="Komentar", null=True, blank=True)
    post = models.ForeignKey(Post, related_name="comment", verbose_name="Post Yang Dikomentar",
                             on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} comment at {self.post.title}"
