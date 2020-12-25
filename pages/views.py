from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request,*args,**kargs):
    print(request)
    print(args, kargs)
    # return HttpResponse("HEHEHEHE")
    return render(request, 'home.html', {})
