from django.urls import path
from . import views

app_name = 'papermodels'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:model_id>/', views.project, name='project'),
    path('upload/', views.upload, name='upload'),
]
