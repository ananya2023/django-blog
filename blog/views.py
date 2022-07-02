from django.shortcuts import redirect, render, get_object_or_404, reverse
from .models import Post, Tag
from django.views.generic import View
from .utils import DetailObjectMixin, CreateObjectMixin, UpdateObjectMixin, DeleteObjectMixin
from .forms import TagForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html',
                  context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostDetail(DetailObjectMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(DetailObjectMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, CreateObjectMixin, View):
    model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class PostCreate(LoginRequiredMixin, CreateObjectMixin, View):
    model = PostForm
    template = 'blog/post_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, UpdateObjectMixin, View):
    model = Tag
    template = 'blog/tag_update.html'
    form_class = TagForm
    raise_exception = True


class PostUpdate(LoginRequiredMixin, UpdateObjectMixin, View):
    model = Post
    template = 'blog/post_update.html'
    form_class = PostForm
    raise_exception = True


class TagDelete(DeleteObjectMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'
    raise_exception = True


class PostDelete(DeleteObjectMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'posts_list_url'
    raise_exception = True
