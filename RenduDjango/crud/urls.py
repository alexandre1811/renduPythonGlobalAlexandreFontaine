from django.urls import path
from . import views

app_name = 'crud'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('details/<int:id>', views.details, name='details'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
