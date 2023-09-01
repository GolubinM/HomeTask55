from django.urls import path
from .views import *

app_name = 'papermodels'

urlpatterns = [
    path('', projects, name='projects'),
    path('<int:model_id>/', project, name='project'),
    path('upload/', upload, name='upload'),
    path('register/', RegisterUser.as_view(), name='register'),
    # path("login/", LoginUser.as_view(), name='login'),
    path("logout/", logout_user, name="logout"),
]
