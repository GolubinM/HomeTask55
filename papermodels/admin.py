from django.contrib import admin
from .models import PaperModels,PaperModelsCategories,Contacts

# Register your models here.
admin.site.register(PaperModels)
admin.site.register(PaperModelsCategories)
admin.site.register(Contacts)
