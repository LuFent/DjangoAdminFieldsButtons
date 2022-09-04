from django.shortcuts import render

# Create your views here.
def catch_button(request):
    print(request.json)