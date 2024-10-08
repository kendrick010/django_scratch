from django.urls import path

from blog.views import (
    ArticleListView,
    ArticleDetailView
)

app_name = "articles"
urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article_detail'),
]