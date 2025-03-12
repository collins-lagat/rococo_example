import { defineStore } from 'pinia';
import api from "./api"

export const useAuthStore = defineStore('auth', {
  state: () => {
    const token = localStorage.getItem('token')
    return {
      token,
    }
  },
  getters: {
    isAuthenticated: (state) => {
      return !!state.token
    },
    user: (state) => {
      return state.user
    },
  },
  actions: {
    async signUp(firstName, lastName, email) {
      const response = await api.auth.signUp(firstName, lastName, email)
      const data = await response.json()

      if (!response.ok && data?.message) {
        throw new Error(data.message)
      }

      if (!response.ok) {
        throw new Error("Unknown error")
      }

      return data
    },
    async login(email, password) {
      const response = await api.auth.login(email, password)
      const data = await response.json()

      if (!response.ok && data?.message) {
        throw new Error(data.message)
      }

      if (!response.ok || !data.token) {
        throw new Error("Unknown error")
      }

      if (data.token) {
        this.token = data.token
      }

      return data
    },
    async newPassword(verificationCode, password, confirmPassword) {
      const response = await api.auth.newPassword(verificationCode, password, confirmPassword)
      const data = await response.json()

      if (!response.ok && data?.message) {
        throw new Error(data.message)
      }

      if (!response.ok) {
        throw new Error("Unknown error")
      }

      return data
    },
  },
})

export const useAccountStore = defineStore('account', {
  state: () => {
    return {
      user: null,
    }
  },
  actions: {
    async get() {
      const { token } = useAuthStore()
      const response = await api.account.get(token)
      const data = await response.json()

      if (!response.ok && data?.message) {
        throw new Error(data.message)
      }

      if (!response.ok) {
        throw new Error("Unknown error")
      }

      if (data?.user) {
        this.user = data.user
      }
      return data
    },
  },
})
