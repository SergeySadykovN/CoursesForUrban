from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('course/create/', views.course_create, name='course_create'),
    path('course/<int:pk>/delete/', views.course_delete, name='course_delete'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
]
