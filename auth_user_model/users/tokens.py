 
# 自定义配置JWT token属性
from rest_framework_simplejwt.tokens import RefreshToken

# rest_framework_simplejwt 默认使用 Django 的 SECRET_KEY 作为签名密钥
# 导入 RefreshToken JWT令牌的标准实现
class CustomToken(RefreshToken):
    # CustomToken类 继承 RefreshToken 具有其所有功能 并可进行自定义
    # 可以在 JWT 的载荷中添加自定义字段
    @classmethod # 一个类方法 通过类本身调用
    def for_user(cls, user):
        token = cls() # cls() 创建CustomToken的新实例
        token.set_user(user) # 调用set_user方法 将用户信息添加到令牌中
        return token # 返回配置好的CustomToken实例

    def set_user(self, user):
        # 添加令牌的载荷(payload)添加自定义字段
        self.payload.update({
            'username': user.username,
            'student_number': getattr(user, 'student_number', ''),
            'class_name': getattr(user, 'class_name', ''),
            'gender': getattr(user, 'gender', '') # ''为使用该属性默认值
        })
        self.user = user # 用户实例存储在 self.user 中

    @property # 将 access_token 方法标记为属性 可以像访问属性一样访问这个方法
    def access_token(self):
        # super().access_token
        # 调用父类 RefreshToken 的 access_token 方法来获取标准的访问令牌
        token = super().access_token
        token.payload.update({ # 更新访问令牌的载荷以包含自定义字段
            'username': self.user.username,
            'student_number': getattr(self.user, 'student_number', ''),
            'class_name': getattr(self.user, 'class_name', ''),
            'gender': getattr(self.user, 'gender', '')
        })
        return token