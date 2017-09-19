from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.


class index(View):
    def get(self,request):
        return HttpResponse("hello!! this is host")
