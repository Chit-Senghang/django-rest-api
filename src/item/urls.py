# urls.py
from django.urls import path

from src.item.item_controller import get_all_items, get_item, create_item, update_item, delete_item

urlpatterns = [
    path('items/', get_all_items, name='get-all-items'),
    path('items/<int:pk>/', get_item, name='get-item'),
    path('items/create/', create_item, name='create-item'),
    path('items/update/<int:pk>/', update_item, name='update-item'),
    path('items/delete/<int:pk>/', delete_item, name='delete-item'),
]
