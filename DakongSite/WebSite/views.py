# WebSite/views.py
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)



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

from django.http import JsonResponse
from .models import MediaFile

def get_media_files(request):
    media_files = MediaFile.objects.all()
    data = [
        {
            "name": file.name,
            "url": request.build_absolute_uri(file.file.url),
            "description": file.description,
        }
        for file in media_files
    ]
    return JsonResponse({"media_files": data})

# WebSite/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# class HomePageAPI(APIView):
#     @swagger_auto_schema(
#         operation_description="Get homepage content including news, products, and toolbar items.",
#         responses={200: openapi.Response(description="Homepage data retrieved successfully")}
#     )
#     def get(self, request):
#         # Fetch the latest homepage content, news, products
#         homepage_content = HomePageContent.objects.all().first()
#         latest_news = Article.objects.language().all()[:3]
#         featured_products = Product.objects.language().all()[:3]
#         toolbar_items = Toolbar.objects.all()

#         data = {
#             'homepage_content': {
#                 'headline': homepage_content.safe_translation_getter('headline', any_language=True) if homepage_content else '',
#                 'subheadline': homepage_content.safe_translation_getter('subheadline', any_language=True) if homepage_content else '',
#                 'promotional_image': homepage_content.promotional_image.url if homepage_content and homepage_content.promotional_image else ''
#             },
#             'latest_news': [
#                 {'title': article.title, 'link': f'/news/{article.pk}/'} for article in latest_news
#             ],
#             'featured_products': [
#                 {'name': product.name, 'link': f'/products/{product.pk}/'} for product in featured_products
#             ],
#             'toolbar_items': [
#                 {'label': item.safe_translation_getter('label', any_language=True), 'description': item.safe_translation_getter('description', any_language=True) if hasattr(item, 'description') else '', 'link': Toolbar.APP_LINKS.get(item.link, item.link)} for item in toolbar_items
#             ],
#             'current_language': request.LANGUAGE_CODE
#         }
#         return Response(data)


# class NewsAPI(APIView):
#     @swagger_auto_schema(
#         operation_description="Get all news articles.",
#         responses={200: openapi.Response(description="News data retrieved successfully")}
#     )
#     def get(self, request):
#         from News.models import Article
#         articles = Article.objects.language().all()
#         data = [
#             {'title': article.title, 'content': article.content, 'link': f'/news/{article.pk}/'} for article in articles
#         ]
#         return Response(data)


# class ProductsAPI(APIView):
#     @swagger_auto_schema(
#         operation_description="Get all products.",
#         responses={200: openapi.Response(description="Products data retrieved successfully")}
#     )
#     def get(self, request):
#         from Products.models import Product
#         products = Product.objects.language().all()
#         data = [
#             {'name': product.name, 'description': product.description, 'price': product.price, 'link': f'/products/{product.pk}/'} for product in products
#         ]
#         return Response(data)


# class MediaAPI(APIView):
#     @swagger_auto_schema(
#         operation_description="Get all media files.",
#         responses={200: openapi.Response(description="Media data retrieved successfully")}
#     )
#     def get(self, request):
#         from Media.models import MediaFile
#         media_files = MediaFile.objects.all()
#         data = [
#             {'name': media_file.name, 'file_url': media_file.file.url, 'uploaded_at': media_file.uploaded_at} for media_file in media_files
#         ]
#         return Response(data)

from rest_framework.viewsets import ModelViewSet
from .models import ToolbarItem
from .serializers import ToolbarItemSerializer

from rest_framework.viewsets import ModelViewSet
from .models import ToolbarItem
from .serializers import ToolbarItemSerializer

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import ToolbarItem
from .serializers import ToolbarItemSerializer

class ToolbarItemViewSet(ModelViewSet):
    """
    ToolbarItem 的視圖集，支持 CRUD 和多語處理。
    """
    queryset = ToolbarItem.objects.all().order_by('position')  # 按 position 排序
    serializer_class = ToolbarItemSerializer    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_visible']  # 支持按 is_visible 過濾

    def get_serializer_context(self):
        """
        傳遞語言代碼到序列化器。
        """
        context = super().get_serializer_context()
        language_code = self.request.query_params.get('languageCode', 'en')
        context['language_code'] = language_code
        return context

logger.info("Homepage view loaded successfully.")

