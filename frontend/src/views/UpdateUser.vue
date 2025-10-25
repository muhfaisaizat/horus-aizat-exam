<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="bg-white p-8 rounded shadow-md w-full max-w-md">
      <h2 class="text-2xl font-bold text-center mb-6">UPDATE USER</h2>
      
      <form class="space-y-4" @submit.prevent="handleUpdateUser">
        <div>
          <label class="block mb-1 font-medium" for="nama">Nama Lengkap</label>
          <input
            type="text"
            id="nama"
            v-model="form.nama"
            placeholder="Masukkan nama lengkap"
            class="w-full px-3 py-2 border border-indigo-400 rounded focus:outline-none focus:ring-2 focus:ring-indigo-300"
          />
        </div>

        <div>
          <label class="block mb-1 font-medium" for="email">Email</label>
          <input
            type="email"
            id="email"
            v-model="form.email"
            placeholder="Masukkan email"
            class="w-full px-3 py-2 border border-indigo-400 rounded focus:outline-none focus:ring-2 focus:ring-indigo-300"
          />
        </div>

        <div>
          <label class="block mb-1 font-medium" for="username">Username</label>
          <input
            type="text"
            id="username"
            v-model="form.username"
            placeholder="Masukkan username"
            class="w-full px-3 py-2 border border-indigo-400 rounded focus:outline-none focus:ring-2 focus:ring-indigo-300"
          />
        </div>

        <div class="flex justify-between gap-3">
          <button
            type="submit"
            class="w-full bg-indigo-400 text-white py-2 rounded hover:bg-indigo-500 transition-colors"
          >
            Update
          </button>
          <button
            type="button"
            @click="handleBack"
            class="w-full bg-gray-300 text-gray-700 rounded-lg hover:bg-gray-400 transition-colors"
          >
            Kembali
          </button>
        </div>
      </form>
    </div>

    <!-- Notifikasi -->
    <Notification
      :open="notifOpen"
      :title="notifTitle"
      :message="notifMessage"
      :type="notifType"
      @close="notifOpen = false"
    />
  </div>
</template>

<script>
import Notification from "../components/Notification.vue";

export default {
  components: { Notification },
  data() {
    return {
      form: {
        nama: "",
        email: "",
        username: "",
      },
      userId: null,
      notifOpen: false,
      notifTitle: "",
      notifMessage: "",
      notifType: "info",
    };
  },
  async created() {
    // Ambil userId dari router state
    this.userId = history.state.userId;
    if (!this.userId) {
      this.$router.push("/dashboard");
      return;
    }

    // Ambil data user dari store
    const user = await this.$store.dispatch("getUserById", this.userId);
    if (user) {
      this.form.nama = user.nama;
      this.form.email = user.email;
      this.form.username = user.username;
    }
  },
  methods: {
    handleBack() {
      this.$router.push("/dashboard");
    },

    async handleUpdateUser() {
      // Validasi input kosong
      if (!this.form.nama || !this.form.email || !this.form.username) {
        this.showNotif("Form Tidak Lengkap", "Semua field harus diisi", "error");
        return;
      }

      try {
        await this.$store.dispatch("updateUser", {
          id: this.userId,
          nama: this.form.nama,
          email: this.form.email,
          username: this.form.username,
        });

        this.showNotif("Berhasil", "User berhasil diupdate", "success");

        // Setelah beberapa detik, kembali ke dashboard
        setTimeout(() => {
          this.$router.push("/dashboard");
        }, 1500);

      } catch (err) {
        console.error("Gagal update user:", err);
        this.showNotif("Error", err.response.data.detail, "error");
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
