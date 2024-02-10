from django.shortcuts import render,redirect
from django.http import HttpResponse
from albums.forms import album_form
from . import forms
from albums.models import albums_Model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class add_album_view(CreateView):
    model = albums_Model
    form_class = album_form
    template_name = 'add_album.html'
    success_url =  reverse_lazy("add_album")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class edit_album_view(UpdateView):
    model = albums_Model
    form_class = album_form
    pk_url_kwarg='id'
    template_name = 'add_album.html'
    success_url = reverse_lazy("add_album")




