import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/register/': {
        target: 'http://127.0.0.1:8000',  // Django 后端 API 地址
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/register/, '')
      },
      '/login/': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/login/, '')
      },
      '/userinfo/': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/userinfo/, '')
      },
      '/token/refresh/': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/token\/refresh/, '')
      }
    }
  }
})
