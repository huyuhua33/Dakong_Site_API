from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    """
    為用戶生成 JWT 訪問和刷新令牌，並添加自定義數據
    """
    refresh = RefreshToken.for_user(user)

    refresh['role'] = user.role  # 添加用戶角色到令牌
    refresh['username'] = user.username

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
}
