<template>
  <el-container style="height: 100vh;">
    <el-header>
      <div class="header-content">
        <el-menu mode="horizontal" default-active="1" class="custom-menu">
          <el-menu-item index="1">
            <router-link to="/login">登录</router-link>
          </el-menu-item>
          <el-menu-item index="2">
            <router-link to="/register">注册</router-link>
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

<script setup>
import { ElContainer, ElHeader, ElMain, ElFooter } from 'element-plus'
</script>

<style scoped>
.header-content {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

/* 确保 el-menu 占满容器宽度 */
.custom-menu {
  justify-content: center;
  width: 100%; /* 使菜单宽度自适应容器 */
}

/* 调整 el-menu-item 样式 */
.el-menu-item {
  min-width: 120px;  /* 增加最小宽度 */
  padding: 0 20px;  /* 增加内边距 */
  text-align: center;
  white-space: nowrap;  /* 禁止换行 */
  overflow: visible;  /* 避免裁剪文本 */
  text-overflow: clip;  /* 禁用省略号 */
}

/* router-link 样式 */
.router-link {
  text-decoration: none;
  color: inherit;
}

.footer-content {
  text-align: center;
  padding: 10px;
  background: #f5f5f5;
}
</style>