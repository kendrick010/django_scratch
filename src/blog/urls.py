from django.urls import path

from blog.views import (
    ArticleListView
)

app_name = "articles"
urlpatterns = [
    path('blog/', ArticleListView.as_view(), name='article_list'),
]