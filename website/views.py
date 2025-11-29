from django.shortcuts import render , redirect
from django.contrib import messages
from django.http import HttpResponse , HttpResponseRedirect
from website.models import Contact , Newsletter
from website.forms import NameForm , ContactForm , NewsletterForm
# Create your views here.
def index_view(request):
    
    return render(request , 'website/index.html')

def about_view(request):
    return render(request , "website/about.html")

def contact_view(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.name = 'ناشناس'
            form.save()
            
            messages.add_message(request , messages.SUCCESS,'your ticket submited successfily')
             
        else:
            messages.add_message(request , messages.ERROR , 'your ticket didnt submited')
             
      
    form = ContactForm()
    return render(request , 'website/contact.html',{'form':form , })

def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
           
            
            return HttpResponse('done')
        else :
            return HttpResponse('not valid')


    
    form = ContactForm()

    return render(request , 'website/test.html' , {'form':form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('website:index')
    else :
            return redirect('website:index')


    form = ContactForm()
    return render(request , 'website/contact.html',{'form':form})