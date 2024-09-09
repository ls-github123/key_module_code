<template>
    <el-form :model="form" :rules="rules" ref="registerForm" label-width="100px" class="register-form">
      <el-form-item label="用户名" prop="username">
        <el-input v-model="form.username" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input type="password" v-model="form.password" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="邮箱" prop="email">
        <el-input v-model="form.email" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="学号" prop="student_number">
        <el-input v-model="form.student_number" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="班级" prop="class_name">
        <el-input v-model="form.class_name" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="性别" prop="gender">
        <el-select v-model="form.gender" placeholder="选择性别">
          <el-option label="男" value="M"></el-option>
          <el-option label="女" value="F"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">提交</el-button>
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
          username: [{ required: true, message: '请输入用户名!', trigger: 'blur' }],
          password: [{ required: true, message: '请设置密码!', trigger: 'blur' }],
          email: [{ required: true, message: '请输入邮箱信息', trigger: 'blur' }],
          student_number: [{ required: true, message: '请输入学号', trigger: 'blur' }],
          class_name: [{ required: true, message: '请输入班级', trigger: 'blur' }],
          gender: [{ required: true, message: '请选择性别', trigger: 'change' }]
        }
      }
    },
    methods: {
      async onSubmit() {
        this.$refs.registerForm.validate(async (valid) => {
          if (valid) {
            try {
              const response = await axios.post('http://127.0.0.1:8000/users/register/', this.form)
              ElMessage.success('账户注册成功!')
            } catch (error) {
              ElMessage.error('注册失败: ' + error.response.data.detail)
            }
          } else {
            ElMessage.error('请正确填写注册表单信息!')
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