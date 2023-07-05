from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.shortcuts import render
from knowledgebase.models import Knowledge, Tag

def index(request): 
    return render(request, template_name='knowledgebase/index.html', context={
        "knowledge": Knowledge.objects.all(),
        "tags": Tag.objects.all(),
    })

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

class KnowledgeByTagView(ListView):
    model = Knowledge
    template_name = 'knowledgebase/knowledge_by_tag.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(tags__name=self.kwargs['name'])
    
    def get_context_data(self, **kwargs):
        context = super(KnowledgeByTagView, self).get_context_data()
        context['current_tag_pk'] = Tag.objects.filter(name=self.kwargs['name']).first().pk
        return context

class TagCreateView(CreateView):
    model = Tag
    fields = '__all__'

class TagUpdateView(UpdateView):
    model = Tag
    fields = '__all__'

class TagDeleteView(DeleteView):
    model = Tag
    fields = '__all__'
    success_url = '/'

class TagDetailView(DetailView):
    model = Tag
    fields = '__all__'