from django.shortcuts import render
from django.http import HttpResponse
from .models import Party

def party_list(request):
    parties = Party.objects.all()
    output = ', '.join([str(party) for party in parties])
    return HttpResponse(output)
