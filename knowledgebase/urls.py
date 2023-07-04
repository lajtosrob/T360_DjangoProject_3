from django.urls import path

from knowledgebase import views

urlpatterns = [
    path('knowledge/create', views.KnowledgeCreateView.as_view(), name='knowledge-create'),
    path('knowledge/update/<int:pk>', views.KnowledgeUpdateView.as_view(), name='knowledge-update')
]
