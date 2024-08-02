from django.urls import path
from . import views

urlpatterns = [
    path('', views.ice_cream_main, name='ice_cream_main'),
    path('icecreams', views.ice_cream_list, name='ice_cream_list'),
    
    path('ice_cream/<int:pk>/', views.ice_cream_detail, name='ice_cream_detail'),
    path('ice_cream/<int:pk>/reviews/', views.ice_cream_reviews, name='ice_cream_reviews'),
    path('ice_cream/<int:pk>/information/', views.ice_cream_information, name='ice_cream_information'),
    path('ice_cream/<int:pk>/add_review/', views.add_review, name='add_review'),
    path('ice_cream/<int:pk>/add_information/', views.add_information, name='add_information'),
    path('review/<int:pk>/delete/', views.delete_review, name='delete_review'),
]
