from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from rest_framework import viewsets

from .models import Blog

# Create your views here.
@require_http_methods(["Get"])
def show_creators(request):
    response = {}
    try:
        creators = Blog.object.filter()
        response['list'] = json.loads(serializers.serialize("json", creators))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["Get"])
def show_blogs(request):
    response = {}
    try:
        creators = Blog.object.filter()
        response['list'] = json.loads(serializers.serialize("json", creators))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)