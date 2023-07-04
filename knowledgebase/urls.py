from django.urls import path

from knowledgebase import views

urlpatterns = [
    path('knowledge/create', views.KnowledgeCreateView.as_view(), name='knowledge-create')
]
