from django.shortcuts import render

import json
# Create your views here.
def home(request):
 
   return render(request, 'home/home.html')


def contact(request):
 
   return render(request, 'home/contact.html')

def blogHome(request):
    return render(request, 'home/home.html')
