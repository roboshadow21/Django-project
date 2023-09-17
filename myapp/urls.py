from django.urls import path
from . import views
from .views import get_orders, get_sorted_orders, upload_image, edit_product

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('orders/<int:user_id>/', get_orders, name='get_orders'),
    path('sorted/<int:user_id>/<int:days>/', get_sorted_orders, name='get_sorted_orders'),
    path('upload/', upload_image, name='upload_image'),
    path('edit/', edit_product, name='edit_product'),
]