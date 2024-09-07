<template>
    <el-container style="padding: 20px;">
      <el-table :data="userInfo" stripe>
        <el-table-column prop="username" label="Username" />
        <el-table-column prop="email" label="Email" />
        <el-table-column prop="student_number" label="Student Number" />
        <el-table-column prop="class_name" label="Class" />
        <el-table-column prop="gender" label="Gender" />
      </el-table>
    </el-container>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  import { ElMessage } from 'element-plus'
  
  const userInfo = ref([])
  const router = useRouter()
  
  const fetchUserInfo = async () => {
    try {
      const token = localStorage.getItem('token')
      if (!token) {
        throw new Error('没有令牌!')
      }
  
      const response = await axios.get('http://127.0.0.1:8000/users/userinfo/', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
      userInfo.value = response.data
    } catch (error) {
      ElMessage.error('Failed to fetch user information: ' + error.message)
      router.push('/login')
    }
  }
  
  onMounted(() => {
    fetchUserInfo()
  })
  </script>
  
  <style scoped>
  /* 样式可根据需要调整 */
  </style>