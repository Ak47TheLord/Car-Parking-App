from django.urls import path
from .views_api import *

urlpatterns = [
    path('carpark', list_slot, name='api-slot-list'),
    path('carpark/add', create_slot, name='api-slot-add'),
    path('carpark/park', park_slot, name='api-slot-park'),
    path('carpark/<int:pk>/unpark', unpark_slot, name='api-slot-unpark'),
    path('carpark/<int:pk>/delete', delete_slot, name='api-slot-delete'),
    path('carpark/<int:pk>/update', update_slot, name='api-slot-update')

]
