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
        # 如果路徑是 /swagger/ 或 /admin/，不進行重定向 # TODO: move 邏輯錯誤 應該不能有額外
        print(f"Request Path Info: {request.path_info}")

        if request.path_info.startswith('/admin/'):
            return self.get_response(request)
        try:
            resolve(request.path_info)  # 嘗試解析路由
        except Resolver404:
            return redirect('/swagger/')  # 未匹配則重定向到 /swagger/
        return self.get_response(request)

