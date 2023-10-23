from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver


def home(request):
    return HttpResponse("Here's the response")


@receiver(request_finished)
def post_request_receiver(sender, **kwargs):
    print("Request finished!")