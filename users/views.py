from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello Django!</h1>")


def profile(request):
    context = {
        "name": "CCJX",
        "age": 27,
        "height": 167,
        "weight": 75.6,
    }

    return JsonResponse(context)
