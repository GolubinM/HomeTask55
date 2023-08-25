from django.db import models


# Create your models here.
class PaperModelsCategories(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='papermodels/images')

    def __str__(self):
        return self.title


class PaperModels(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='papermodels/images')
    upload = models.FileField(upload_to='papermodels/uploads')
    category = models.ForeignKey(PaperModelsCategories, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
