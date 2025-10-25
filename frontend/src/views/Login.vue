<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-100">
        <div class="w-full max-w-sm bg-white p-8 rounded-lg shadow-md">
            <h2 class="text-2xl font-bold text-center mb-6">LOGIN</h2>

            <form @submit.prevent="handleLogin" class="space-y-4">
                <div>
                    <label class="block text-gray-700 mb-1">Username</label>
                    <input v-model="username" type="text" placeholder="Masukkan username"
                        class="w-full px-3 py-2 border border-indigo-400 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-300" />
                </div>

                <div>
                    <label class="block text-gray-700 mb-1">Password</label>
                    <input v-model="password" type="password" placeholder="Masukkan password"
                        class="w-full px-3 py-2 border border-indigo-400 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-300" />
                </div>

                <div class="flex justify-between items-center mt-6">
                    <button type="submit"
                        class="px-4 py-2 bg-indigo-400 text-white rounded-lg hover:bg-indigo-500 transition">
                        Login
                    </button>
                    <button type="button" @click="goToRegister"
                        class="px-4 py-2 bg-gray-300 text-gray-700 rounded-lg hover:bg-gray-400 transition">
                        Registrasi
                    </button>
                </div>
            </form>
        </div>

        <Notification :open="notifOpen" :title="notifTitle" :message="notifMessage" :type="notifType"
            @close="notifOpen = false" />
    </div>
</template>

<script>
import { mapActions } from "vuex";
import Notification from "../components/Notification.vue";

export default {
    name: "Login",
    components: { Notification },
    data() {
        return {
            username: "",
            password: "",
            notifOpen: false,
            notifTitle: "",
            notifMessage: "",
            notifType: "",
        };
    },
    methods: {
        ...mapActions(["login"]),

        async handleLogin() {
            try {
                await this.login({
                    username: this.username,
                    password: this.password,
                });
                this.$router.push("/dashboard");
            } catch (err) {
                this.showNotif(
                    "Gagal!",
                    err.response.data.detail || "Terjadi kesalahan server.",
                    "error"
                );
            }
        },

        goToRegister() {
            this.$router.push("/register");
        },


        showNotif(title, message, type) {
            this.notifTitle = title;
            this.notifMessage = message;
            this.notifType = type;
            this.notifOpen = true;

            setTimeout(() => {
                this.notifOpen = false;
            }, 3000);
        },
    },
};
</script>
