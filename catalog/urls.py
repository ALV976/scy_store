from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, products_list, products_detail
from catalog.views import contacts

app_name = CatalogConfig.name

urlpatterns = [
    #path('', home, name='home'),
    #path('contacts/', contacts, name='home'),
    path('', products_list, name='products_list'),
    path('catalog/<int:pk>/', products_detail, name='products_detail')
]
