from django.urls import path, include
from . import views
from .views import info_list, delete_record, manage_items

urlpatterns = [

    path('',views.home, name = 'home'),
    path('information', views.all_info, name = "borrow-info"),
    path('add_info', views.add_info, name='add-info'),
    path('search', views.search, name = 'search'),
    path('', info_list, name='info_list'),
    path('delete_record/<int:record_id>/', delete_record, name='delete_record'),
    path('ajax/item-search/', views.item_search, name='item_search'),
    path('manage-items/', views.manage_items, name='manage_items'),
    path('add-item/', views.add_item, name='add_item'),
    path('edit-item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete-item/<int:item_id>/', views.delete_item, name='delete_item')
]