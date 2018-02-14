from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Party, Clown
from .forms import PartyForm, ClownForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def party_list(request):


def party_detail(request, pk):


def post_party(request):


class PartyDelete(DeleteView):


class PartyUpdate(UpdateView):
