from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from knowledgebase.models import Knowledge

class KnowledgeCreateView(CreateView):
    model = Knowledge
    fields = '__all__'

class KnowledgeUpdateView(UpdateView):
    model = Knowledge
    fields = '__all__'

class KnowledgeDeleteView(DeleteView):
    model = Knowledge
    fields = '__all__'
    success_url = '/'

class KnowledgeDetailView(DetailView):
    model = Knowledge
    fields = '__all__'