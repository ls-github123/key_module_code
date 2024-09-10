<template>
  <el-container style="padding: 20px;">
    <!-- 用户信息表格 -->
    <el-table :data="[userInfo]" stripe>
      <el-table-column prop="username" label="用户名" />
      <el-table-column prop="email" label="邮箱" />
      <el-table-column prop="student_number" label="学号" />
      <el-table-column prop="class_name" label="班级" />
      <el-table-column
          prop="gender"
          label="性别"
          :formatter="formatGender"
      />
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
      throw new Error('用户未登录!')
    }

    // 发起请求获取用户信息
    const response = await axios.get('http://127.0.0.1:8000/users/userinfo/', {
      headers: {
        Authorization: `Bearer ${token}`  // 携带token进行身份验证
      }
    })
    
    userInfo.value = response.data  // 将用户信息保存到userInfo中
  } catch (error) {
    ElMessage.error('无法获取到用户信息: ' + error.message)  // 显示错误信息
    router.push('/login')  // 如果获取失败，跳转到登录页面
  }
}

// 格式化性别
const formatGender = (row, column, cellValue) => {
  return cellValue === 'M'? '男':'女';
}

// 退出登录，清除token
const handleLogout = () => {
  localStorage.removeItem('token')  // 清除本地存储的token
  ElMessage.warning('已退出登录')  // 显示成功信息
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