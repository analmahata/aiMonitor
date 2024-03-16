from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, 'index.html')

def contact(requests):
    return render(requests, 'contact.html')