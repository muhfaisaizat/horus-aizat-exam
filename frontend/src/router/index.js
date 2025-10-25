import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Dashboard from "../views/Dashboard.vue";
import UpdateUser from "../views/UpdateUser.vue";
import store from "../store/auth";

const routes = [
    { path: "/", redirect: "/login" },
    { path: "/login", component: Login },
    { path: "/register", component: Register },
    {
        path: "/dashboard",
        component: Dashboard,
        meta: { requiresAuth: true },
    },
    {
        path: "/updateuser",
        component: UpdateUser,
        name: 'UpdateUser',
        meta: { requiresAuth: true },
    },
];

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
});


router.beforeEach((to, from, next) => {
    const token = store.state.token || localStorage.getItem("token");

    if (to.meta.requiresAuth && !token) {
        next("/login");
    } else if ((to.path === "/login" || to.path === "/register") && token) {
        next("/dashboard");
    } else {
        next();
    }
});

export default router;
