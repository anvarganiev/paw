from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import LoginForm


def home_view(request,*args,**kargs):
    print(request)
    print(args, kargs)
    # return HttpResponse("HEHEHEHE")
    return render(request, 'home.html', {})


def login_view(request,*args,**kargs):
    print(request)
    print(args, kargs)
    # return HttpResponse("HEHEHEHE")
    return render(request, 'home.html', {})


def get_logindata(request,*args,**kargs):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'mypage.html', {'form': form})