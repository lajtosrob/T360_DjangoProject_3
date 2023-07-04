from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from knowledgebase.models import Knowledge

class KnowledgeCreateView(CreateView):
    model = Knowledge
    fields = '__all__'

