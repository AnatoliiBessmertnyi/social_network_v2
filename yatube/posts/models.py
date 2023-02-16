from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts'
    )

    class Meta:  # Объявили мета класс и в нем метод сортировки
        ordering = ['-pub_date']

# Очень слабо понял этот момент, работает все и без этого
    #def __str__(self):  # Добавлен метод __str__
        #return s[i:j] = t ' slice of s from i to j' = 't это отрезок s от i до j'


class Group(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title
