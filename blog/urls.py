from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogHome,name='blogHome'), 
    path('postComment', views.postComment, name="postComment"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('<str:slug>', views.blogPost,name='blogPost'), 
    
]