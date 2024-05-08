from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import BlogpostUpdateView, BlogpostListView, BlogpostDetailView, BlogpostDeleteView

##from catalog.views import home
# from catalog.views import ProductsListView, ProductsDetailView
# from catalog.views import contacts

app_name = BlogsConfig.name

urlpatterns = [
    # path('', home, name='home'),
    # path('contacts/', contacts, name='home'),
    path('create/', BlogpostUpdateView.as_view(), name='create'),
    path('list/', BlogpostListView.as_view(), name='blogpost_list'),
    path('blogs/view/<int:pk>/', BlogpostDetailView.as_view(), name='view'),
    path('edit/<int:pk>', BlogpostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', BlogpostDeleteView.as_view(), name='delete'),

]
