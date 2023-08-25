from django.shortcuts import render, get_object_or_404
from .models import PaperModels, PaperModelsCategories


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

# def upload_file(request):
#     # обработать создание записи в БД, загрузку файлов с эскизом и pdf-файлом
#     # https://djangodoc.ru/3.1/ref/models/fields/#django.db.models.FileField
#     if request.method == 'POST':
#         form = ModelFormWithFileField(request.POST, request.FILES)
#         if form.is_valid():
#             # file is saved
#             form.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = ModelFormWithFileField()
#     return render(request, 'upload.html', {'form': form})
