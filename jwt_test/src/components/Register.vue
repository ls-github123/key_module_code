<template>
    <el-form :model="form" :rules="rules" ref="registerForm" label-width="100px" class="register-form">
      <el-form-item label="Username" prop="username">
        <el-input v-model="form.username" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="Password" prop="password">
        <el-input type="password" v-model="form.password" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="Email" prop="email">
        <el-input v-model="form.email" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="Student Number" prop="student_number">
        <el-input v-model="form.student_number" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="Class Name" prop="class_name">
        <el-input v-model="form.class_name" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="Gender" prop="gender">
        <el-select v-model="form.gender" placeholder="Select Gender">
          <el-option label="Male" value="male"></el-option>
          <el-option label="Female" value="female"></el-option>
          <el-option label="Other" value="other"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">Register</el-button>
      </el-form-item>
    </el-form>
  </template>
  
  <script>
  import axios from 'axios'
  import { ElMessage } from 'element-plus'
  
  export default {
    data() {
      return {
        form: {
          username: '',
          password: '',
          email: '',
          student_number: '',
          class_name: '',
          gender: '',
        },
        rules: {
          username: [{ required: true, message: 'Please input your username', trigger: 'blur' }],
          password: [{ required: true, message: 'Please input your password', trigger: 'blur' }],
          email: [{ required: true, message: 'Please input your email', trigger: 'blur' }],
          student_number: [{ required: true, message: 'Please input your student number', trigger: 'blur' }],
          class_name: [{ required: true, message: 'Please input your class name', trigger: 'blur' }],
          gender: [{ required: true, message: 'Please select your gender', trigger: 'change' }]
        }
      }
    },
    methods: {
      async onSubmit() {
        this.$refs.registerForm.validate(async (valid) => {
          if (valid) {
            try {
              const response = await axios.post('/register/', this.form)
              ElMessage.success('Registration successful!')
            } catch (error) {
              ElMessage.error('Registration failed: ' + error.response.data.detail)
            }
          } else {
            ElMessage.error('Please fill in the form correctly.')
            return false
          }
        })
      }
    }
  }
  </script>
  
  <style>
  .register-form {
    max-width: 500px;
    margin: 0 auto;
  }
  </style>