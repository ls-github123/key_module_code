from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView # JWT刷新
from . import views 


urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'), # 用户注册
    path('login/', views.UserLoginView.as_view()), # 用户登录
    path('userinfo/', views.UserDetailView.as_view(), name='user_detail'), # 获取当前用户信息
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # 刷新JWT Token
]
