from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from groups.models import Group
from posts.models import Post,Comment
from posts.forms import PostForm,CommentForm
# Create your views here.

class PostCreateView(LoginRequiredMixin,generic.CreateView):
    login_url = '/accounts/login/'
    model      = Post
    form_class = PostForm

    template_name = "post/post_form.html"

    def form_valid(self, form):
        form.instance.auther = self.request.user
        form.instance.group  = get_object_or_404(Group,slug=self.kwargs['group'])
        return super().form_valid(form)   

class PostUpdateView(LoginRequiredMixin,generic.UpdateView):
    login_url = '/accounts/login/'
    model      = Post
    form_class = PostForm

    template_name = "post/post_form.html"    

class PostDeleteView(LoginRequiredMixin,generic.DeleteView):
    login_url = '/accounts/login/'
    model      = Post
    success_url = reverse_lazy("post:posts")
    template_name = "post/post_delete.html"

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post/post_detail.html"


class CommentCreateView(LoginRequiredMixin,generic.CreateView):
    login_url = '/accounts/login/'
    model      = Comment
    form_class = CommentForm

    template_name = "post/comment_form.html"

    def form_valid(self, form):
        form.instance.auther = self.request.user
        form.instance.post   = get_object_or_404(Post,pk=self.kwargs['post']) 
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin,generic.UpdateView):
    login_url = '/accounts/login/'
    model      = Comment
    form_class = CommentForm

    template_name = "post/comment_form.html"    

class CommentDeleteView(LoginRequiredMixin,generic.DeleteView):
    login_url = '/accounts/login/'
    model      = Comment
    template_name = "post/comment_delete.html"

    def get_success_url(self):
        comment    = get_object_or_404(Comment,pk=self.kwargs.get('pk'))
        return reverse_lazy("post:post_detail", kwargs={'pk': comment.post.pk})