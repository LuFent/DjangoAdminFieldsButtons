from django.shortcuts import render
from django.http import HttpResponse
import json
from django.apps import apps

def catch_button(request):
    request_data = json.loads(request.read())
    apps.get_model(app_label='adminbuttons', model_name='testclass')
    print(request_data)
    return HttpResponse('OK')