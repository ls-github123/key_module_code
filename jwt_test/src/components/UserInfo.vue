<template>
  <el-container style="padding: 20px;">
    <!-- 用户信息表格 -->
    <el-table :data="[userInfo]" stripe>
      <el-table-column prop="username" label="Username" />
      <el-table-column prop="email" label="Email" />
      <el-table-column prop="student_number" label="Student Number" />
      <el-table-column prop="class_name" label="Class" />
      <el-table-column prop="gender" label="Gender" />
    </el-table>

    <!-- 退出按钮 -->
    <el-button type="danger" @click="handleLogout" style="margin-top: 20px;">
      退出
    </el-button>
  </el-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'

// 定义用户信息的状态
const userInfo = ref({})
const router = useRouter()

// 异步请求用户信息
const fetchUserInfo = async () => {
  try {
    const token = localStorage.getItem('token')  // 从localStorage获取token
    if (!token) {
      throw new Error('没有令牌!')
    }

    // 发起请求获取用户信息
    const response = await axios.get('http://127.0.0.1:8000/users/userinfo/', {
      headers: {
        Authorization: `Bearer ${token}`  // 携带token进行身份验证
      }
    })
    
    userInfo.value = response.data  // 将用户信息保存到userInfo中
  } catch (error) {
    ElMessage.error('Failed to fetch user information: ' + error.message)  // 显示错误信息
    router.push('/login')  // 如果获取失败，跳转到登录页面
  }
}

// 退出登录，清除token
const handleLogout = () => {
  localStorage.removeItem('token')  // 清除本地存储的token
  ElMessage.success('已退出登录')  // 显示成功信息
  router.push('/login')  // 跳转回登录页面
}

// 在组件挂载时执行
onMounted(() => {
  fetchUserInfo()
})
</script>

<style scoped>
/* 你可以根据需要调整样式 */
</style>