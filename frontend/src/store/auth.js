import { createStore } from 'vuex'
import api from '../services/api'

const store = createStore({
  state() {
    return {
      user: null,
      token: localStorage.getItem('token') || null,
    }
  },

  mutations: {
    setUser(state, user) {
      state.user = user
    },
    setToken(state, token) {
      state.token = token
      localStorage.setItem('token', token)
    },
    logout(state) {
      state.token = null
      localStorage.removeItem('token')
    },
  },

  actions: {
    async register(_, payload) {
      const query = new URLSearchParams(payload).toString()
      return await api.post(`/users/register?${query}`)
    },

    async login({ commit }, payload) {
      const query = new URLSearchParams(payload).toString();
      const res = await api.post(`/users/login?${query}`);
      commit('setToken', res.data.token);
      return res;
    },

    async logout({ commit }) {
      commit('logout')
    },

    async getUser({ commit, state }) {
      try {
        const token = state.token || localStorage.getItem('token')
        if (!token) throw new Error('Token tidak tersedia')

        const res = await api.get('/users', {
          headers: { Authorization: `Bearer ${token}` },
        })

        commit('setUser', res.data) 
        return res.data
      } catch (error) {
        console.error('Gagal mengambil user:', error)
        return null
      }
    },

     async getUserById({ state }, userId) {
      try {
        const token = state.token || localStorage.getItem('token')
        if (!token) throw new Error('Token tidak tersedia')

        const res = await api.get(`/users/${userId}`, {
          headers: { Authorization: `Bearer ${token}` },
        })

        return res.data
      } catch (error) {
        console.error('Gagal mengambil user berdasarkan ID:', error)
        return null
      }
    },

     async deleteUser({ state }, userId) {
      try {
        const token = state.token || localStorage.getItem('token')
        if (!token) throw new Error('Token tidak tersedia')

        const res = await api.delete(`/users/${userId}`, {
          headers: { Authorization: `Bearer ${token}` },
        })

        return res.data
      } catch (error) {
        console.error('Gagal menghapus user:', error)
        throw error
      }
    },

    async updateUser({ state }, { id, username, email, nama }) {
      try {
        const token = state.token || localStorage.getItem('token')
        if (!token) throw new Error('Token tidak tersedia')

        const query = new URLSearchParams({ username, email, nama }).toString()

        const res = await api.put(`/users/${id}?${query}`, null, {
          headers: { Authorization: `Bearer ${token}` },
        })

        return res.data
      } catch (error) {
        console.error('Gagal update user:', error)
        throw error
      }
    },
  },
})

export default store
