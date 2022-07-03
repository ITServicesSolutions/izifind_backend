from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'customer/index.html')

def services(request):
    return render(request, 'customer/service.html')

def about(request):
    return render(request, 'customer/about.html')

def contact(request):
    return render(request, 'customer/contact.html')
