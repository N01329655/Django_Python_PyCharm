# my file for urls in my_app01
from django.urls import path
from .views import homePageView

urlpatterns = [

    path('', homePageView, name='home'),

]


