from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post', views.post_new, name='post'),
    path('detail/<int:pk>', views.post_detail, name='detail'),
]