from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group, User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import PostForm

posts_per_page = 10


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, posts_per_page) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, posts_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author).order_by('-pub_date')
    paginator = Paginator(posts, posts_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }

    return render(request, 'posts/post_detail.html', context)

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = request.user.id
            user = request.user.username
            post.save()
            return redirect('posts:profile', user)
        return render(request, 'posts/create_post.html', context)
    form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create_post.html', context)

#       if request.method == 'POST':
#         form = ExchangeForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             title = form.cleaned_data['title']
#             artist = form.cleaned_data['artist']
#             genre = form.cleaned_data['genre']
#             price = form.cleaned_data['price']
#             comment = form.cleaned_data['comment']
#             return redirect('/thank-you/')
#         return render(request, 'index.html', {'form': form})
#     form = ExchangeForm()
#     return render(request, 'index.html', {'form': form}) 
    
# def thank_you(request):
#     return render(request, 'thankyou.html')
#     if request.method == 'POST':
#     form = ExchangeForm(request.POST)
#     context = {

#     }

#     return render(request, 'posts/post_create.html', context)