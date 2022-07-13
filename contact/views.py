from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
# from .form import MassegeModelForm
# from .models import MessageModel

class ContactView(TemplateView):
    template_name = "contact/contact.html"



    

# class ContactView(CreateView):
#     model = MessageModel
#     form_class = MessageModelForm
#     template_name = 'contact/contact.html'

#     def get_success_url(self):
#         return redirect ('contact')