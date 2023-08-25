from django.contrib import admin
from .models import PaperModels,PaperModelsCategories

# Register your models here.
admin.site.register(PaperModels)
admin.site.register(PaperModelsCategories)
