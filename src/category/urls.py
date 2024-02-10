from django.urls import path

from .category_controller import get_category, create_category

urlpatterns = [
    path('category/', get_category, name='get-all-category'),
    path('category/create/', create_category, name='create-category')

]
