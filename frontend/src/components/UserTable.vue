<template>
  <div class="p-6 bg-white rounded-lg shadow-md w-full">
    <div class="flex justify-between items-center mb-4">
      <div class="grid gap-3">
        <h2 class="text-lg font-semibold text-gray-900">Users</h2>
        <SearchBar v-model="searchQuery" />
      </div>
      <button
        @click="$emit('logout')"
        class="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700 transition-colors"
      >
        Log Out
      </button>
    </div>

    <div class="overflow-x-auto mt-4">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Username</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Nama Lengkap</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Aksi</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="user in filteredUsers" :key="user.id">
            <td class="px-6 py-4 whitespace-nowrap text-gray-900">{{ user.id }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-gray-500">{{ user.username }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-gray-500">{{ user.nama }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-gray-500">{{ user.email }}</td>
            <td class="px-6 py-4 whitespace-nowrap">
              <button
                @click="$emit('updateUser', user)"
                class="text-indigo-600 hover:underline mr-2"
              >
                Edit
              </button>
              <button
                @click="$emit('deleteUser', user)"
                class="text-red-600 hover:underline"
              >
                Hapus
              </button>
            </td>
          </tr>

          <tr v-if="filteredUsers.length === 0">
            <td colspan="5" class="text-center text-gray-500 py-4">
              Tidak ada data ditemukan.
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import SearchBar from "./SearchBar.vue";

export default {
  name: "UserTable",
  components: { SearchBar },
  props: {
    users: {
      type: Array,
      required: true,
    },
  },
  data() {
    return { searchQuery: "" };
  },
  computed: {
    filteredUsers() {
      // Jika belum mengetik apa pun, tampilkan semua user
      if (!this.searchQuery) return this.users;

      const q = this.searchQuery.toLowerCase();

      // Filter berdasarkan kolom tertentu (kecuali aksi)
      return this.users.filter(
        (user) =>
          String(user.id).toLowerCase().includes(q) ||
          user.username?.toLowerCase().includes(q) ||
          user.nama?.toLowerCase().includes(q) ||
          user.email?.toLowerCase().includes(q)
      );
    },
  },
};
</script>
