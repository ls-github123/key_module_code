<template>
    <el-form :model="loginForm" ref="loginFormRef" label-width="120px" class="login-form">
      <el-form-item label="Username" :rules="[{ required: true, message: 'Please input your username', trigger: 'blur' }]">
        <el-input v-model="loginForm.username" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="Password" :rules="[{ required: true, message: 'Please input your password', trigger: 'blur' }]">
        <el-input v-model="loginForm.password" type="password" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleLogin">Login</el-button>
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
      const token = response.data.token
      if (!token) {
        throw new Error('未获取到TOKEN')
      }
      localStorage.setItem('token', token)
      ElMessage.success('登录成功')
      router.push('/userinfo')
    } catch (error) {
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
  