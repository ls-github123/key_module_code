from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser  # 确保导入AnonymousUser类
# 用户注册序列化器
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = models.CustomUser
        fields = ('username', 'email', 'password', 'student_number', 'class_name', 'gender')
    
    # 重写create方法添加用户信息
    def create(self, validated_data):
        user = models.CustomUser.objects.create_user(
            username = validated_data['username'],
            student_number = validated_data['student_number'],
            password = validated_data['password'],
            email = validated_data.get('email'),
            class_name = validated_data.get('class_name'),
            gender = validated_data.get('gender'),
        )
        return user
    
# 用户详情序列化器
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('username', 'email', 'student_number', 'class_name', 'gender')
    def to_representation(self, instance):
        # 检查用户是否是AnonymousUser
        if isinstance(instance, AnonymousUser):
            return {
                'detail':'用户未登录'
            }
        return super().to_representation(instance)