from django.urls import path
from .views import *

urlpatterns = [
    path('test',test,name='test'),
    path('sendmail',send_mail_to_all,name='sendmail'),
]