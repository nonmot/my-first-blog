from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post', views.post_new, name='post'),
    path('detail/<int:pk>', views.post_detail, name='detail'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('find', views.find, name='find'),
]