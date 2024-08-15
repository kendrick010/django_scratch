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