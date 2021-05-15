# my file for urls in my_app01
from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [

    path('', HomePageView.as_view(), name='homepage'),
    path('about/', AboutPageView.as_view(), name='aboutpage'),
]


