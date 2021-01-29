from django.urls import path

from .views import (
    HomePageView
)

app_name = 'core'


urlpatterns = [
    path("", HomePageView.as_view(), name="index")
    # path("", ContactView.as_view(), name="index"),
    # path("", SubscriberView.as_view(), name='index')
]