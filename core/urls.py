from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('track/<int:order_id>/', views.order_tracking, name='order_tracking'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]