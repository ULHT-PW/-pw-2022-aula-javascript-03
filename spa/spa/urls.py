from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_view),
    path('sections/<int:section>', views.section_view)
]
