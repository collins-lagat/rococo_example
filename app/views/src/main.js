import '@quasar/extras/material-icons/material-icons.css';
import { createPinia } from 'pinia';
import { Quasar } from 'quasar';
import 'quasar/src/css/index.sass';
import { createApp } from 'vue';
import { createRouter, createWebHashHistory } from "vue-router";
import App from './App.vue';
import Container from './components/container.vue';
import MainLayout from './layouts/main.vue';
import Index from './pages/index.vue';
import NewPassword from './pages/new-password.vue';
import SignIn from './pages/sign-in.vue';
import SignUp from './pages/sign-up.vue';
import { useAuthStore } from './store';

const pinia = createPinia()
const app = createApp(App)

app.component('Container', Container)

app.use(Quasar, {
  plugins: {}, // import Quasar plugins and add here
})

app.use(pinia)

const routes = [
  {
    path: '/',
    component: MainLayout,
    children: [
      {
        path: '',
        component: Index,
        meta: {
          auth: true,
          title: 'Home',
        },
      },
      {
        path: 'new-password/:token',
        component: NewPassword,
        meta: {
          auth: false,
          title: 'New Password',
        }
      },
      {
        path: 'sign-in',
        component: SignIn,
        meta: {
          auth: false,
          title: 'Sign In',
        }
      },
      {
        path: 'sign-up',
        component: SignUp,
        meta: {
          auth: false,
          title: 'Sign Up',
        }
      },
    ]
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  if (to.meta.auth && !authStore.isAuthenticated) {
    next("/sign-in")
  } if (!to.meta.auth && authStore.isAuthenticated) {
    next("/")
  }
  next()
})

app.use(router)
app.mount('#app')
