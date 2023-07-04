from django.contrib import admin
from knowledgebase import models

# Register your models here.
admin.site.register(models.Tag)
admin.site.register(models.Knowledge)