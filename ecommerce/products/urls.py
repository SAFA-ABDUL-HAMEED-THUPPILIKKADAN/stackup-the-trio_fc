from django.urls import path
from .views import index,details,create,delete,update,product_list



app_name='products'

urlpatterns = [
    path('',index,name='list'),
    path('<int:id>/',details,name='details'),
    path('create/',create,name='create'),
    path('<int:id>/delete/',delete,name='delete'),
    path('<int:id>/update/',update,name='update'),
    path('product_list/', product_list, name='product_list'),
] 

