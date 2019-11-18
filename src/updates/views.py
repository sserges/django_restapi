from django.http import JsonResponse
from django.shortcuts import render


def update_model_detail_view(request):
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    return JsonResponse(data)

