from django.urls import path

from .views import index, catalog, detail_device
from .views import other_page

app_name = 'main'
urlpatterns = [
    path('detail/<int:pk>/', detail_device, name='detail_device'),
    path('catalog/', catalog, name='catalog'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
