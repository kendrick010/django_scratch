from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from .forms import ArticleModelForm
from .models import Article

# Create your views here.
class ArticleListView(ListView):
    queryset = Article.objects.all()    # looks for blog/<modelname>_list.html

class ArticleDetailView(DetailView):
    queryset = Article.objects.all()    # looks for blog/<modelname>_list.html

    # We can limit what objects get rendered by detail view
    # queryset = Article.objects.filter(id__gt=1)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)