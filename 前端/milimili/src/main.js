import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import elementplus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import axios from 'axios'

const app = createApp(App).use(store).use(router).use(elementplus)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
app.mount("#app")