import { createApp } from 'vue'
import { Quasar } from 'quasar'
import { createPinia } from 'pinia'

import './style.css'
// Import icon libraries
import '@quasar/extras/material-icons/material-icons.css'

// Import Quasar css
import 'quasar/src/css/index.sass'

import App from './App.vue'

const pinia = createPinia()
const app = createApp(App)

app.use(Quasar, {
  plugins: {}, // import Quasar plugins and add here
})
app.use(pinia)

app.mount('#app')
