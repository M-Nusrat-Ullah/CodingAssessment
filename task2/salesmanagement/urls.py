from django.urls import path
from . import views

urlpatterns = [
    path('api/sales/', views.create_sales_data, name='create_sales_data'),
    path('api/sales/<int:pk>/', views.sales_data_detail, name='sales_data_detail'),
    path('report/', views.generate_report, name='generate_report'),
]