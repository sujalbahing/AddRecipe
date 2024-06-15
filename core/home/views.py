from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    peoples = [
        {'name': 'Sujal Rai', 'age': 20},
        {'name': 'Rabin Rai', 'age': 14},
        {'name': 'Subin Rai', 'age': 21},
        {'name': 'Ayush Tamang', 'age': 16},
        {'name': 'Sushant Dahal', 'age': 80},
    ]

    vegetables = [
        'Pumpkin', 'Tomato', 'Onion'
    ]
    return render(request, 'home/index.html', {'peoples': peoples, 'vegetables': vegetables},)


def about(request):
    context = {'page': "About"}
    return render(request, 'home/about.html',context)

def contact(request):
    context = {'page': "Contact"}
    return render(request, 'home/contact.html',context)


def success_page(request):
    return HttpResponse("<h1>Hey This is a Success page!</h1>")
