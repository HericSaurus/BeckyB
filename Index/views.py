from django.shortcuts import render,redirect,get_object_or_404
from .forms import ContactForm
from .models import ContactUs


# Create your views here.

def index(request):
    return render (request, 'index/index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None) 
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('contact',)
    else:
        form = ContactForm()
        stuff_for_frontend = {'form' : form}
        return render (request,'index/contact.html',stuff_for_frontend)

def our_story(request):
    return render (request, 'index/our_story.html')

def portfolio(request):
    return render (request, 'index/portfolio.html')

def portfolio_detail_1(request):
    return render (request, 'index/portfolio_detail_1.html')