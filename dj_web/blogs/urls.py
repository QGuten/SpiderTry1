from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'show_creators$', show_creators, ),
]

