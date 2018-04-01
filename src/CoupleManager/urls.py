from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', UserList.as_view(), name='list')
]