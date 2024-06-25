from django.urls import path, include
from . import views
from .views import info_list, delete_record

urlpatterns = [

    path('',views.home, name = 'home'),
    path('information', views.all_info, name = "borrow-info"),
    path('add_info', views.add_info, name='add-info'),
    path('search', views.search, name = 'search'),
    path('', info_list, name='info_list'),
    path('delete_record/<int:record_id>/', delete_record, name='delete_record'),
]