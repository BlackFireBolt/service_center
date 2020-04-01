from django.urls import path

from .views import index, catalog, detail_device
from .views import other_page, slider_test

app_name = 'main'
urlpatterns = [
    path('slider/', slider_test, name='slider_test'),
    path('detail/<int:pk>/', detail_device, name='detail_device'),
    path('catalog/', catalog, name='catalog'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
