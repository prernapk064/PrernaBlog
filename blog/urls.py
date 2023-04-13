from . import views
from django.urls import path

urlpatterns = [
    
    path('', views.Home, name='redir'),
    path('home/', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('home/create/', views.PostCreate.as_view(), name='PostCreate'),
    path('home/update/<slug:slug>/', views.PostUpdate.as_view(), name='PostUpdate'),
    path('home/delete/<slug:slug>/', views.PostDelete.as_view(), name='PostDelete'),
]