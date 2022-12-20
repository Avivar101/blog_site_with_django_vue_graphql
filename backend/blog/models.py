from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = RichTextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"slug": self.slug})


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    subname = models.CharField(max_length=55, blank=True)
    slug = models.SlugField(max_length=255, unique=True, default="slug")
    body = models.TextField(default="cat body")
    date_created = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(blank=True, null=True)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT, default=User)

    def __str__(self):
        return self.name
