from django.urls import path, include

from . import views
urlpatterns = [



    path('',views.imag2),
    path('a',views.display),
]
