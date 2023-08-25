from django.shortcuts import render, get_object_or_404

from .forms import AddPostForm
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
