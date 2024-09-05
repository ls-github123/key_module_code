from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# 自定义用户管理器
class CustomUserManager(BaseUserManager):
    def create_user(self, username, student_number, password=None, email=None, **extra_fields):
        if not username:
            raise ValueError('用户必须提供用户名')
        if not student_number:
            raise ValueError('用户必须提供学号')
        if not password:
            raise ValueError('密码不能为空')
        
        email = self.normalize_email(email) if email else None
        user = self.model(username=username, student_number=student_number, email=email, **extra_fields)
        user.set_password(password) # 设置密码 存储密码并进行加密
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, student_number, password=None, email=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('超级用户必须设置staff')
        if extra_fields.get('is_superuser') is not None:
            raise ValueError('超级用户必须设置superuser')
        
        return self.create_user(username, student_number, password, email, **extra_fields)
    
# 自定义用户模型
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('用户名', max_length=100, unique=True, null=False) # 用户名
    email = models.EmailField('邮箱', null=True, blank=True, default=None) # 邮箱可为空
    class_name = models.CharField('班级', max_length=50, null=False) # 班级
    student_number = models.CharField('学号', max_length=25, unique=True)
    gender_choices = (
        ('M', '男'),
        ('F', '女'),
    )
    gender = models.CharField('性别', null=False, max_length=1, choices=gender_choices)
    is_active = models.BooleanField(default=True) # 是否活跃
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'username' # 使用用户名作为登录标识
    REQUIRED_FIELDS = ['student_number', 'class_name', 'gender'] # 创建superuser时必填的字段
    
    def __str__(self):
        return self.username