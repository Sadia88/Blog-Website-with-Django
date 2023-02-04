from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('contact', views.contact,name='contact'),
    path('about', views.about,name='about'),
    path('delete', views.delete,name='delete'),
    path('edit', views.edit,name='edit'),
   
    path('search', views.search,name='search'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('ajax', views.ajax, name="ajax"),
    
    
]