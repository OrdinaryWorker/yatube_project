from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """ Class for adding groups on site """
    title = models.CharField(max_length=200, verbose_name='Group name')
    slug = models.SlugField(unique=True, verbose_name='Web address')
    description = models.TextField(max_length=600,
                                   verbose_name='Group description')

    def __str__(self):
        return self.title


class Post(models.Model):
    """ Class for making posts with given attributes"""
    text = models.TextField(verbose_name="Post's text")
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Publication date')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Author',
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Group name',
        related_name='posts'
    )

    class Meta:
        ordering = ['-pub_date']
