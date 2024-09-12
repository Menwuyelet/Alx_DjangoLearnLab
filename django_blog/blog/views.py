from django.shortcuts import render, redirect
from .forms import UserCreation, profileUpdate
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
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

 
# class RegisterView(CreateView)
