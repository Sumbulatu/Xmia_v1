from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'core/index.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'core/dashboard.html')


def support(request):
    return render(request, 'core/support.html')
