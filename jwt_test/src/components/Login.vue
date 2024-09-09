<template>
    <el-form :model="loginForm" ref="loginFormRef" label-width="120px" class="login-form">
      <el-form-item label="用户名" :rules="[{ required: true, message: '请输入用户名', trigger: 'blur' }]">
        <el-input v-model="loginForm.username" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="密码" :rules="[{ required: true, message: '请输入用户密码', trigger: 'blur' }]">
        <el-input v-model="loginForm.password" type="password" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleLogin">登录</el-button>
      </el-form-item>
    </el-form>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  import { ElMessage } from 'element-plus'
  
  const loginForm = ref({
    username: '',
    password: ''
  })
  
  const router = useRouter()
  
  const handleLogin = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/users/login/', loginForm.value)
    const token = response.data.access
    if (!token) {
      throw new Error('未获取到TOKEN')
    }
    console.log('Token: ', token) // 调试信息
    localStorage.setItem('token', token)
    console.log('Token已保存') // 调试信息
    ElMessage.success('登录成功')
    router.push('/userinfo')
  } catch (error) {
    console.error('Error during login: ', error) // 调试信息
    ElMessage.error('Login failed: ' + error.message)
  }
}

  </script>
  
  <style scoped>
  .login-form {
    max-width: 400px;
    margin: auto;
    padding: 20px;
  }
  </style>
  