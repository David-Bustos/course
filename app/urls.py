from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'home'),
    path('create', views.create, name = 'create'),
    path('delete/<number>', views.delete, name = 'delete'),
    # path('comments/<id>', views.comments, name = 'comments'),
]
