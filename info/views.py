from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Contact, Publication


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = {
            'publication_list': Publication.objects.all(),
            'activ': Publication.objects.filter(is_activ=True)
        }
        return context

class ContactView(TemplateView):
    template_name = 'contact.html'

class PublicationView(TemplateView):
    template_name = 'publication-detail.html'

    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']
        context = {
            'publication': Publication.objects.get(id=publication_pk),
            'publication_list': Publication.objects.all()

        }
        return context

def client_message(request):
    print(request.POST)


    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

    Contact.objects.create(name=name, email=email, subject=subject, message=message)

    return redirect('contact-list')


