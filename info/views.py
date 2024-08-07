from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Contact


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class PublicationView(TemplateView):
    template_name = 'publication-detail.html'

def client_message(request):
    print(request.POST)


    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

    Contact.objects.create(name=name, email=email, subject=subject, message=message)

    return redirect('contact-list')


