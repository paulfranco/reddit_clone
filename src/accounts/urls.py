from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url('signup/', views.signup, name='signup'),
    url('login/', views.loginview, name='login'),
]
