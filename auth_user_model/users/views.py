from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserRegisterSerializer, UserDetailSerializer
from django.contrib.auth import authenticate
from .tokens import CustomToken # 导入自定义的Token类

# 用户注册视图
# 继承自 generics.CreateAPIView，这是 Django REST framework 提供的用于处理创建资源的通用视图
class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all() # 模型实例 获取数据库中信息
    permission_classes = [AllowAny] # 设定访问权限 允许所有用户访问
    serializer_class = UserRegisterSerializer # 关联相关序列化器
    
    # 自定义create方法 用于接收用户提交的注册信息
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data) # 获取序列化器实例 并将请求数据传递
        if serializer.is_valid(): # 检查数据是否合规
            user = serializer.save() # 数据合规 保存数据
            # refresh = RefreshToken.for_user(user)  # 生成JWT Token
            refresh = CustomToken.for_user(user) # 生成/使用自定义的Token类
            return Response({
                "user":UserDetailSerializer(user).data, # 返回用户数据
                "refresh": str(refresh), # 获取刷新令牌数据
                "access": str(refresh.access_token), # 获取登录令牌数据
            }, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# 用户登录视图
# 继承APIView
class UserLoginView(APIView):
    permission_classes = [AllowAny] # 允许所有用户访问
    
    # 定义post请求方法
    def post(self, request, *args, **kwargs):
        login_username = request.data.get('username')
        login_password = request.data.get('password')
        user = authenticate(username=login_username, password=login_password) # 验证用户
        print(f"输出user_authenticate返回结果:{user}")
        
        if user is not None:
            # refresh = RefreshToken.for_user(user)  # 生成JWT Token
            refresh = CustomToken.for_user(user) # 使用自定义的Token类
            return Response ({
                "user": UserDetailSerializer(user).data, # 返回用户数据
                "refresh": str(refresh), # 刷新令牌信息
                "access":str(refresh.access_token), # 登录令牌信息
            }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "用户名或密码不正确"}, status=status.HTTP_401_UNAUTHORIZED)
        
# 获取当前用户注册详情信息视图
# 继承自APIView 通用API视图类(自定义行为视图)
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated] # 配置访问权限 仅允许已认证用户访问
    
    def get(self, request, *args, **kwargs):
        # 从请求中获取user对象
        # 视图使用了IsAuthenticated, user已是经过认证的用户
        user = request.user
        # 只有已认证用户才能访问
        if user.is_authenticated:
            # is_authenticated 是一个用于检查用户是否已通过身份验证的布尔属性
            # 用户登录验证通过返回True, 否则为False
            # 如果用户已认证，使用 UserDetailSerializer 序列化用户数据并返回
            # 状态码为 200 OK
            serializer = UserDetailSerializer(user)
            # print(serializer)
            return Response(serializer.data)
        else:
            return Response({"detail":"用户未认证"}, status=status.HTTP_401_UNAUTHORIZED)