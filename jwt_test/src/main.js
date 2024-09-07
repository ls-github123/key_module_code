import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from 'axios'
import router from './router' // 引入路由组件

const app = createApp(App)

app.use(router)
app.use(ElementPlus)
app.mount('#app')