# inventory/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Existing URLs
    path('', views.product_list, name='product_list'),
    path('product/new/', views.product_create, name='product_create'),
    path('product/<int:pk>/edit/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),

    path('category/', views.category_list, name='category_list'),
    path('category/new/', views.category_create, name='category_create'),
    path('category/<int:pk>/edit/', views.category_update, name='category_update'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # New URLs
    path('export/xlsx/', views.export_products_xlsx, name='export_products_xlsx'),
    path('product/<int:pk>/change_order_status/', views.change_order_status, name='change_order_status'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
