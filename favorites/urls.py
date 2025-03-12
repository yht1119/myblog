from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:article_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove/<int:article_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('add_like/<int:article_id>/', views.add_like, name='add_like'),
    path('remove_like/<int:article_id>/', views.remove_like, name='remove_like'),
    path('my_favorites/<int:id>/', views.my_favorites, name='my_favorites'),
]
