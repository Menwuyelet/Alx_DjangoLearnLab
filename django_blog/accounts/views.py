from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, UserChangeForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance = request.user)
    return render(request, 'registration/profile.html', {'form': form})


