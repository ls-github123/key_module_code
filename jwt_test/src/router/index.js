// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Register from '../components/Register.vue'
import Login from '../components/Login.vue'
import UserInfo from '../components/UserInfo.vue'  // 导入 UserInfo 组件

const routes = [
  { path: '/register', component: Register },
  { path: '/login', component: Login },
  { path: '/userinfo', component: UserInfo }, // 添加用户信息页面路由
  // 其他路由可以继续添加
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router  // 只导出 router 实例