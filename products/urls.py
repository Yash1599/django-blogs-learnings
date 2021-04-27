from django.urls import path 
from .views import product_delete_view ,product_detail_view ,product_list_view 


app_name = 'products'
urlpatterns =[
    path('<int:id>' , product_detail_view ,name='product'),
    path('<int:id>/delete' , product_delete_view ,name='product-delete'),
]