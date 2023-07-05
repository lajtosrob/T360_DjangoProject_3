from django.urls import path

from knowledgebase import views

urlpatterns = [
    path('', views.index),
    path('knowledge/create/', views.KnowledgeCreateView.as_view(), name='knowledge-create'),
    path('knowledge/view/<int:pk>', views.KnowledgeDetailView.as_view(), name='knowledge-view'),
    path('knowledge/update/<int:pk>', views.KnowledgeUpdateView.as_view(), name='knowledge-update'),
    path('knowledge/delete/<int:pk>', views.KnowledgeDeleteView.as_view(), name='knowledge-delete'),
    path('knowledge/by_tag/<str:name>', views.KnowledgeByTagView.as_view(), name='knowledge-by-tag'),
    path('tag/create/', views.TagCreateView.as_view(), name='tag-create'),
    path('tag/update/<int:pk>', views.TagUpdateView.as_view(), name='tag-update'),
    path('tag/delete/<int:pk>', views.TagDeleteView.as_view(), name='tag-delete'),
]
