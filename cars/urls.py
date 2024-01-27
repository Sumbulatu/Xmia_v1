from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cars_list/', views.cars_list, name='cars_list')
    # path('cars_list/', views.CarsListView.as_view(), name='cars_list'),
    # path('car_detail/<int:car_id>/', views.cars_detail, name='cars_detail'),
    # path('upload/', views.upload_car, name='upload_car'),
    # path('buy/', views.car_info, name='car_info'),
]
