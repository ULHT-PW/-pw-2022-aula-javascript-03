from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_view),
    path('posts', views.posts_view),
]
