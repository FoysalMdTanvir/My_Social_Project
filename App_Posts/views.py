from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    return render(request, 'App_Posts/home.html', context={'title': 'Home | iBook'})
