<template>
  <div class="min-h-screen flex justify-center bg-gray-100">
    <UserTable :users="users" @logout="handleLogOut" @updateUser="handleUpdate" @deleteUser="handleDelete" />

    <Notification :open="notifOpen" :title="notifTitle" :message="notifMessage" :type="notifType"
      :buttonText="notifButtonText" @close="notifOpen = false" @buttonClick="confirmDelete" />
  </div>
</template>

<script>
import UserTable from "../components/UserTable.vue";
import Notification from "../components/Notification.vue";

export default {
  components: { UserTable, Notification },
  data() {
    return {
      users: [],
      notifOpen: false,
      notifTitle: "",
      notifMessage: "",
      notifType: "info",
      notifButtonText: "",
      userToDelete: null,
    };
  },
  async created() {
    await this.fetchUsers();
  },
  methods: {
    async fetchUsers() {
      try {
        const res = await this.$store.dispatch("getUser");
        this.users = res ? res.data || res : [];
      } catch (err) {
        this.$store.dispatch("logout");
        this.$router.push("/login");
      }
    },
    handleLogOut() {
      this.$store.dispatch("logout");
      this.$router.push("/login");
    },
    handleUpdate(user) {
      this.$router.push({
        name: "UpdateUser",
        state: { userId: user.id }
      });
    },
    handleDelete(user) {

      this.userToDelete = user;


      this.notifTitle = "Apakah Anda Yakin Untuk Hapus?";
      this.notifMessage = "Klik tombol Hapus di bawah jika ingin melanjutkan.";
      this.notifType = "info";
      this.notifButtonText = "Hapus";
      this.notifOpen = true;
    },
    async confirmDelete() {
      if (!this.userToDelete) return;

      try {
        await this.$store.dispatch('deleteUser', this.userToDelete.id)
        this.notifOpen = false
        this.userToDelete = null
        this.fetchUsers()
      } catch (err) {
        console.error('Gagal hapus user:', err)
      }
    },
  },
};
</script>
