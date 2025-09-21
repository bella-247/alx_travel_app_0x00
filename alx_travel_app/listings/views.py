from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def ping(request):
    return JsonResponse({'status': 'ok', 'app': 'alx_travel_app'})
