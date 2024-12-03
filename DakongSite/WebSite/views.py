# WebSite/views.py
from django.shortcuts import render
from .models import HomePageContent
from News.models import Article
from Products.models import Product
import logging

logger = logging.getLogger(__name__)


# WebSite/views.py
from django.shortcuts import render
from .models import HomePageContent, Toolbar
from News.models import Article
from Products.models import Product

def homepage(request):
    # Fetch the latest homepage content, news, products, and toolbar items
    homepage_content = HomePageContent.objects.all().first()
    latest_news = Article.objects.language().all()[:3]
    featured_products = Product.objects.language().all()[:3]
    toolbar_items = Toolbar.objects.all()

    context = {
        'homepage_content': homepage_content,
        'latest_news': latest_news,
        'featured_products': featured_products,
        'toolbar_items': toolbar_items,
    }
    return render(request, 'website/home.html', context)

def homepage(request):
    logger.debug("Fetching homepage content, news, and products.")
    # Fetch the latest homepage content, news, and products
    homepage_content = HomePageContent.objects.all().first()
    latest_news = Article.objects.language().all()[:3]
    featured_products = Product.objects.language().all()[:3]

    logger.debug(f"Homepage content: {homepage_content}")
    logger.debug(f"Latest news: {latest_news}")
    logger.debug(f"Featured products: {featured_products}")

    context = {
        'homepage_content': homepage_content,
        'latest_news': latest_news,
        'featured_products': featured_products,
    }
    return render(request, 'website/home.html', context)

logger.info("Homepage view loaded successfully.")
