from django.db import models
from ckeditor.fields import RichTextField


class MediaIcon(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    social = models.ForeignKey(MediaIcon, on_delete=models.CASCADE, related_name='ico')
    redirect = models.CharField(max_length=255, verbose_name="Link Social Media Kamu ")

    def __str__(self):
        return self.social.name


class Profile(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nama Kamu  ")
    nick_name = models.CharField(max_length=255, default="Annisa Maharani", verbose_name="Nama Panggilan")
    desc = RichTextField(verbose_name="Deskripsi Singkat  ")
    profile_img = models.ImageField(upload_to='profile', verbose_name="Foto Profil ")
    social_media = models.ManyToManyField(SocialMedia, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Judul Posting  ")
    link = models.SlugField(max_length=255)
    content = RichTextField(verbose_name="Konten ",
                            config_name='default',
                            external_plugin_resources=[
                                         ('youtube',
                                          '/static/ckeditor_plugins/youtube/youtube/',
                                          'plugin.js')
                                     ],)
    desc = models.TextField(verbose_name="Deskripsi Singkat ")
    keyword = models.TextField(verbose_name="keyword pencarian ")
    date_create = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class MediaManager(models.Model):
    file = models.FileField(upload_to='manager/')

    def __str__(self):
        return str(self.file)

    def delete(self, using=None, keep_parents=False, *args, **kwargs):
        self.delete()
        super().delete(*args, **kwargs)
