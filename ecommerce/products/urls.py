from django.urls import path
from .views import index,details,create,delete,update,product_list,add_to_cart,remove_from_cart



app_name='products'

urlpatterns = [
    path('add_products/',index,name='list'),
    path('<int:id>/',details,name='details'),
    path('create/',create,name='create'),
    path('<int:id>/delete/',delete,name='delete'),
    path('<int:id>/update/',update,name='update'),
    path('', product_list, name='product_list'),
    path('cart/<int:id>/',add_to_cart,name='cart'),
    path('remove_from_cart/<int:id>/', remove_from_cart, name='remove_from_cart'),
    

    
]

    
