<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="bg-white p-8 rounded shadow-md w-full max-w-md">
      <h2 class="text-2xl font-bold text-center mb-6">REGISTRASI AKUN</h2>

      <form class="space-y-4" @submit.prevent="handleRegister">
        <div>
          <label class="block mb-1 font-medium" for="nama">Nama Lengkap</label>
          <input v-model="nama" type="text" id="nama" placeholder="Masukkan nama lengkap"
            class="w-full px-3 py-2 border border-indigo-400 rounded focus:outline-none focus:ring-2 focus:ring-indigo-300" />
        </div>

        <div>
          <label class="block mb-1 font-medium" for="email">Email</label>
          <input v-model="email" type="email" id="email" placeholder="Masukkan email"
            class="w-full px-3 py-2 border border-indigo-400 rounded focus:outline-none focus:ring-2 focus:ring-indigo-300" />
        </div>

        <div>
          <label class="block mb-1 font-medium" for="username">Username</label>
          <input v-model="username" type="text" id="username" placeholder="Masukkan username"
            class="w-full px-3 py-2 border border-indigo-400 rounded focus:outline-none focus:ring-2 focus:ring-indigo-300" />
        </div>

        <div>
          <label class="block mb-1 font-medium" for="password">Password</label>
          <input v-model="password" type="password" id="password" placeholder="Masukkan password"
            class="w-full px-3 py-2 border border-indigo-400 rounded focus:outline-none focus:ring-2 focus:ring-indigo-300" />
        </div>

        <button type="submit"
          class="w-full bg-indigo-400 text-white py-2 rounded hover:bg-indigo-500 transition-colors">
          Registrasi
        </button>
      </form>

      <p class="mt-4 text-center text-gray-600">
        Sudah punya akun?
        <router-link to="/login" class="text-indigo-400 hover:underline">
          Login
        </router-link>
      </p>
    </div>

    <Notification :open="notifOpen" :title="notifTitle" :message="notifMessage" :type="notifType"
      @close="notifOpen = false" />
  </div>
</template>

<script>
import { mapActions } from "vuex";
import Notification from "../components/Notification.vue";

export default {
  name: "RegisterView",
  components: { Notification },
  data() {
    return {
      nama: "",
      email: "",
      username: "",
      password: "",
      notifOpen: false,
      notifTitle: "",
      notifMessage: "",
      notifType: "success",
    };
  },
  methods: {
    ...mapActions(["register"]),

    async handleRegister() {
      if (!this.nama || !this.email || !this.username || !this.password) {
        this.showNotif("Gagal!", "Semua field wajib diisi.", "error");
        return;
      }

      try {
        const res = await this.register({
          nama: this.nama,
          email: this.email,
          username: this.username,
          password: this.password,
        });


        this.showNotif("Berhasil!", res.data.message, "success");

        this.nama = "";
        this.email = "";
        this.username = "";
        this.password = "";

        setTimeout(() => {
          this.$router.push("/login");
        }, 2000);

      } catch (error) {
        // console.error("Register error:", error);
        this.showNotif(
          "Gagal!",
          error.response.data.detail || "Terjadi kesalahan server.",
          "error"
        );
      }
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
