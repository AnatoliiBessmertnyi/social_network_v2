from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group


def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Последние обновления на сайте'
    text = 'Это главная страница проекта Yatube'
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title': title,
        'text': text,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    text = f'Посты группы "{group.title}"'
    # Получаем уникальное название 'title'
    title = f'Записи сообщества "{group.title}"'
    context = {
        'group': group,
        'posts': posts,
        'text': text,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
