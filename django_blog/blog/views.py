from django.shortcuts import render, redirect
from .forms import UserCreation, profileUpdate
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Comment
from django.urls import reverse_lazy
from .forms import post_form, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

def homeView(request):
    return render(request, template_name='blog/base.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('login')
    else:
        form = UserCreation()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = profileUpdate(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return render('profile')
    else:
        form = profileUpdate(instance=request.user)

        context = {
            'form': form,
        }
    return render(request, 'blog/profile.html', context)

 
class post_list(ListView):
    model = Post
    template_name = 'blog/post_list.html' 
    context_object_name = 'posts'

class post_detail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class Add_post(LoginRequiredMixin, CreateView): # this view handles the post publishing action
    model = Post # takes the model "Post"
    form_class = post_form # takes the 'post_form' from .foms.py
    template_name = 'blog/post_create.html' # renders the 'Form.html' from templates/blog
    success_url = reverse_lazy('post_list') # after publishing the post redirects to 'post_list' page
    login_url = 'login' # if the user is not loged in it requires it to login

    def form_valid(self, form): # this method checkes if the user is logged in to post.
        form.instance.author = self.request.user 
        return super().form_valid(form)


class Update_post(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # this view is a viewclass that handles the post editing action it uses the same form and template as add post
    model = Post
    form_class = post_form
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('post_list')    

    def test_func(self): # this method checks the user trying to update the post is the author of the post
        post = self.get_object()
        return self.request.user == post.author 
    
class Delete_post(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # this view is a viewclass that handles the post deleting action it uses the same form and template as add post
    model = Post 
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list') 

    def test_func(self): # this method checks the user trying to update the post is the author of the post
        post = self.get_object()
        return self.request.user == post.author 

 

## Comment views


class Add_comment(LoginRequiredMixin, CreateView): # adds new comment
    model = Comment 
    form_class = CommentForm # takes the 'CommentForm' from .foms.py
    template_name = 'blog/comment_create.html' # renders the 'comment_create.html' from templates/blog
    success_url = reverse_lazy('post_detail') # after publishing the post redirects to 'post_detail' page
    login_url = 'login' # if the user is not loged in it requires it to login

class list_comment(ListView): # list all the comments under specific post 
    model = Comment
    template_name = 'blog/comment_list.html' 
    context_object_name = 'comments'

class Update_comment(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # this view is a viewclass that handles the comment editing action it uses the same form as add comment
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_update.html'
    success_url = reverse_lazy('post_detail')    

    def test_func(self):  # checks if the user trying to edit the commet is the author of the comment
        comment = self.get_object()
        return self.request.user == comment.author
    
class Delete_comment(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # this view is a viewclass that handles the post deleting action it uses the same form and template as add post
    model = Comment 
    template_name = 'blog/comment_delete.html'
    success_url = reverse_lazy('comment_list') 

    def test_func(self):  # checks if the user trying to delete the comment is the user that published the post or the comment
        comment = self.get_object()
        post = post.get_object()
        return self.request.user == post.author or self.request.user == comment.author