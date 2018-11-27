from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, 'index/index.html')

def contact(request):
    return render (request, 'index/contact.html')

def our_story(request):
    return render (request, 'index/our_story.html')

def portfolio(request):
    return render (request, 'index/portfolio.html')

def portfolio_detail(request):
    return render (request, 'index/portfolio_detail.html')