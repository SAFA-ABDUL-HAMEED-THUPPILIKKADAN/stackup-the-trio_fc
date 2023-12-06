
from django.urls import path

from .views import index,details


app_name='categories'

urlpatterns = [
    path('',index,name='list'),
    path('<int:id>/',details,name='details')
    
]
