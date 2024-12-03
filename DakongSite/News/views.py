# News/views.py
# Views for listing articles and viewing article details
from django.views.generic import ListView, DetailView
from .models import Article
import logging

logger = logging.getLogger(__name__)

class ArticleListView(ListView):
    model = Article
    template_name = 'news/article_list.html'
    context_object_name = 'articles'

logger.info("ArticleListView loaded successfully.")

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/article_detail.html'
    context_object_name = 'article'

logger.info("ArticleDetailView loaded successfully.")