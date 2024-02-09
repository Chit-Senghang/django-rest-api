# urls.py
from django.urls import path

from src.item.category.views import get_category, create_category
from src.item.views import get_all_items, get_item, create_item, update_item, delete_item

urlpatterns = [
    path('items/', get_all_items, name='get-all-items'),
    path('items/<int:pk>/', get_item, name='get-item'),
    path('items/create/', create_item, name='create-item'),
    path('items/update/<int:pk>/', update_item, name='update-item'),
    path('items/delete/<int:pk>/', delete_item, name='delete-item'),

    # Category
    path('category/', get_category, name='get-all-category'),
    path('category/create/', create_category, name='create-category')

]
