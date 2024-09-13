from django.shortcuts import render, redirect
from .forms import UserCreation, profileUpdate
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from django.urls import reverse_lazy
from .forms import post_form
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
    template_name = 'blog/listing.html' 
    context_object_name = 'posts'

class post_detail(DetailView):
    model = Post
    template_name = 'blog/viewing.html'


class Add_post(LoginRequiredMixin, CreateView): # this view handles the post publishing action
    model = Post # takes the model "Post"
    form_class = post_form # takes the 'post_form' from .foms.py
    template_name = 'blog/creating.html' # renders the 'Form.html' from templates/blog
    success_url = reverse_lazy('post_list') # after publishing the post redirects to 'post_list' page
    login_url = 'login' # if the user is not loged in it requires it to login

    def form_valid(self, form): # this method checkes if the user is logged in to post.
        form.instance.author = self.request.user 
        return super().form_valid(form)


class Update_post(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # this view is a viewclass that handles the post editing action it uses the same form and template as add post
    model = Post
    form_class = post_form
    template_name = 'blog/editing.html'
    success_url = reverse_lazy('post_list')    

    def test_func(self): # this method checks the user trying to update the post is the author of the post
        post = self.get_object()
        return self.request.user == post.author 
    
class Delete_post(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # this view is a viewclass that handles the post deleting action it uses the same form and template as add post
    model = Post 
    template_name = 'blog/deleting.html'
    success_url = reverse_lazy('post_list') 

    def test_func(self): # this method checks the user trying to update the post is the author of the post
        post = self.get_object()
        return self.request.user == post.author 