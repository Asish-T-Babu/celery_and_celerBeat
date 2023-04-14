from django.shortcuts import render
from django.http import HttpResponse
from .task import test_func
from send_mail_app.task import *

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")