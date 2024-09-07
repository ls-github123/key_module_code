<script setup>
import { ElContainer, ElHeader, ElMain, ElFooter } from 'element-plus'
</script>

<template>
  <el-container style="height: 100vh;">
    <el-header>
      <div class="header-content">
        <el-menu mode="horizontal" default-active="1">
          <el-menu-item index="1">
            <router-link to="/login">Login</router-link>
          </el-menu-item>
          <el-menu-item index="2">
            <router-link to="/register">Register</router-link>
          </el-menu-item>
        </el-menu>
      </div>
    </el-header>
    <el-main>
      <router-view></router-view> <!-- 渲染当前路由的组件 -->
    </el-main>
    <el-footer>
      <div class="footer-content">
        <p>&copy; 2024 Your Company</p>
      </div>
    </el-footer>
  </el-container>
</template>

<style scoped>
.header-content {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.footer-content {
  text-align: center;
  padding: 10px;
  background: #f5f5f5;
}
</style>
