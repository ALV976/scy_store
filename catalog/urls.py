from django.urls import path
from catalog.apps import CatalogConfig
# from catalog.views import home
from catalog.views import ProductsListView, ProductsDetailView

# from catalog.views import contacts

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    # path('contacts/', contacts, name='home'),
    path('', ProductsListView.as_view(), name='products_list'),
    path('catalog/<int:pk>/', ProductsDetailView.as_view(), name='products_detail')
]
