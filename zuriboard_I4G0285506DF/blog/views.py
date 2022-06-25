from ast import Delete
from dataclasses import field
from pyexpat import model
from turtle import update
from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
 model = Post

class PostCreate(generic.CreateView):
 model = Post
 fields = "__all__"
 success_url  = reverse_lazy("blog:all")

class PostDetail(generic.DetailView):
 model = Post

class PostUpdate(generic.UpdateView):
 model = Post
 fields = "__all__"
 success_url  = reverse_lazy("blog:all")

class PostDelete(generic.DeleteView):
 model = Post
 fields = "__all__"
 success_url  = reverse_lazy("blog:all")