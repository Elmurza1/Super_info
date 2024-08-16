from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import Contact, Publication, PublicationComment


# Create your views here.
class HomeView(TemplateView): #TODO:   se&
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        publication_list = Publication.objects.all()
        paginator = Paginator(publication_list, 2)
        page_number = self.request.GET['page']
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'activ': Publication.objects.filter(is_activ=True)
        }
        return context

class SearchView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        search_word = self.request.GET['query']
        context = {

            'publication_list': Publication.objects.filter(is_activ=True).filter(

                Q(title__icontains=search_word) |Q(description__icontains=search_word)

            )
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


class PublicationCommentView(View):

    def post(self, request, *args, **kwargs):
        comment_pk = kwargs['pk']
        publication = Publication.objects.get(id=comment_pk)

        input_name = request.POST['name']
        input_text = request.POST['message']

        PublicationComment.objects.create(publication=publication,name=input_name, text=input_text)

        return redirect('publication-list' ,pk=comment_pk)



