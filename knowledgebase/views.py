from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from knowledgebase.models import Knowledge

class KnowledgeCreateView(CreateView):
    model = Knowledge
    fields = '__all__'

class KnowledgeUpdateView(UpdateView):
    model = Knowledge
    fields = '__all__'

