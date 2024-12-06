# WebSite/views.py
from django.shortcuts import render
from .models import HomePageContent
from News.models import Article
from Products.models import Product
import logging

logger = logging.getLogger(__name__)

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

from django.http import JsonResponse
from django.utils.translation import activate
from .models import PageContent

def get_language_content(request, lang_code):
    activate(lang_code)
    content = PageContent.objects.all()
    data = [
        {
            "slug": item.slug,
            "title": item.safe_translation_getter('title', ''),
            "description": item.safe_translation_getter('description', '')
        }
        for item in content
    ]
    return JsonResponse({"language": lang_code, "content": data})


logger.info("Homepage view loaded successfully.")

