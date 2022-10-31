
from django.shortcuts import render,redirect
from .forms import *
from django.http import *
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.http import require_http_methods

# Create your views here.
def user_login(request):
    return render(request,'login.html')


@require_http_methods(["POST"])
def user_auth(request):
    # if request.method=='POST':
        u= request.POST.get('uname')
        p= request.POST.get('psw')

        user = authenticate(username=u,password=p)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse('invalid username or password')


def user_logout(request):
    logout(request)
    return redirect('login')


def index_page(request):
    return render(request,'index.html')

def user_reg(request):
    if request.method == 'POST':
        form = reg_form(request.POST)
        if form.is_valid():
            d=form.cleaned_data
            u = d['username']
            e = d['email']
            p = d['password']
            User.objects.create_user(username=u,email=e,password=p)
            return redirect('login')
    else:
        form = reg_form()
    return render(request,'reg.html',{'form':form})