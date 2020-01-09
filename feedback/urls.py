from django.urls import path

from .views import FeedBackView

app_name = 'feedback'
urlpatterns = [
    path('feedback/', FeedBackView.as_view(), name='feedback_view'),
]
