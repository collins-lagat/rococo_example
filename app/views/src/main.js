import { createPinia } from 'pinia';
import { Quasar } from 'quasar';
import { createApp } from 'vue';
import { createRouter, createWebHashHistory } from "vue-router";
import './style.css';
import '@quasar/extras/material-icons/material-icons.css';
import 'quasar/src/css/index.sass';
import App from './App.vue';
import Index from './pages/index.vue';
import NewPassword from './pages/new-password.vue';
import SignIn from './pages/sign-in.vue';
import SignUp from './pages/sign-up.vue';

const pinia = createPinia()
const app = createApp(App)

app.use(Quasar, {
  plugins: {}, // import Quasar plugins and add here
})

app.use(pinia)

const routes = [
  {
    path: '/',
    component: Index,
  },
  {
    path: '/new-password',
    component: NewPassword,
  },
  {
    path: '/sign-in',
    component: SignIn,
  },
  {
    path: '/sign-up',
    component: SignUp,
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

app.use(router)
app.mount('#app')
