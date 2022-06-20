from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """ Class for adding groups on site """
    title = models.CharField(max_length=200, verbose_name='Название группы')
    slug = models.SlugField(unique=True, verbose_name='Вэб адрес')
    description = models.TextField(max_length=600,
                                   verbose_name='Описание группы')

    def __str__(self):
        return self.title


class Post(models.Model):
    """ Class for making posts with given attributes"""
    text = models.TextField(
        verbose_name="Текст поста",
        help_text="Текст нового поста"
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Название группы',
        related_name='posts',
        help_text="Группа, к которой будет относиться пост "
    )

    def __str__(self):
        return self.text[:15]

    class Meta:
        ordering = ['-pub_date']
