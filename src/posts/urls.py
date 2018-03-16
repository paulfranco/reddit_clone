from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url('create/', views.create, name='create'),

]
