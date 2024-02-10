from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from musicians.forms import musicians_form
from musicians.models import musician_Model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



class add_musician_view(CreateView):
    model = musician_Model
    form_class = musicians_form
    template_name = 'add_musician.html'
    success_url =  reverse_lazy("add_musician")
    def form_valid(self, form):
        return super().form_valid(form)
    


class edit_musician_view(UpdateView):
    model = musician_Model
    form_class = musicians_form
    pk_url_kwarg='id'
    template_name = 'add_musician.html'
    success_url = reverse_lazy("homepage")


class delete_musician_view(DeleteView):
    model = musician_Model
    template_name="home.html"
    pk_url_kwarg='id'
    success_url = reverse_lazy("homepage")
    

