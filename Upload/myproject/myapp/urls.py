
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload1', views.upload1,name='upload1'),
    path('upload', views.upload,name='upload'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('view_book/<int:pk>/', views.view_book, name='view_book'),
]
