from django.urls import path
from .views import SubscribermailView, ContactUsView, JoinUsView

urlpatterns = [
    path('api/subscribermail/', SubscribermailView.as_view(), name='subscriber_mail'),
    path('api/contactus/', ContactUsView.as_view(), name='contact_us'),
    path('api/joinus/', JoinUsView.as_view(), name='join_us'),
]