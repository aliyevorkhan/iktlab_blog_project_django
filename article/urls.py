from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('add_article/', views.add_article, name="add_article"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('comment/<int:id>', views.comment, name="comment"),

]


