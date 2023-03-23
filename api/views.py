from django.http.response import JsonResponse
from django.shortcuts import render


def inde(request):
    return render(request,'index.html')

def get_chart(_request):

    chart={}

    return JsonResponse(chart)i
