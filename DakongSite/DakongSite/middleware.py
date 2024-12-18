# middleware tools

from django.shortcuts import redirect
from django.urls import resolve, Resolver404

class RedirectUnmatchedURLMiddleware:
    """
    將未匹配的 URL 重定向到 /swagger/
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            # 嘗試解析當前的路徑
            resolve(request.path_info)
        except Resolver404:
            # 如果路由未匹配，重定向到 /swagger/
            return redirect('/swagger/')
        return self.get_response(request)
