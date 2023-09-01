from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse

from .forms import AddPostForm, RegisterUserForm, LoginUserForm
from .models import *
from django.contrib import messages


def main(request):
    return render(request, 'papermodels/main.html')


def projects(request):
    projects = PaperModelsCategories.objects.all()
    return render(request, 'papermodels/projects.html', {"projects": projects})


def project(request, model_id):
    category_title = get_object_or_404(PaperModelsCategories, pk=model_id).title
    project = PaperModels.objects.filter(category_id=model_id)
    context = {"project": project,
               "id": model_id,
               "cat_title": category_title}
    return render(request, 'papermodels/project.html', context=context)


def upload(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AddPostForm()
    return render(request, 'papermodels/upload.html', {'form': form})


def contacts(request):
    conts = Contacts.objects.all()
    return render(request, 'papermodels/contacts.html', {'contacts': conts})


def logout_user(request):
    logout(request)
    return redirect('login')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'papermodels/register.html'
    success_url = reverse_lazy('login')  # возвращаемся на форму в случае успеха


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'papermodels/login.html'

    def get_success_url(self):
        return reverse_lazy('login')  # возвращаемся на форму в случае успеха
