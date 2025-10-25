import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import router from './router';
import auth from './store/auth'; // Vuex store

const app = createApp(App);

app.use(router);
app.use(auth); // <-- daftar store ke app
app.mount('#app');
