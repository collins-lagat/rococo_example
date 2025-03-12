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
    signUp(firstName, lastName, email) {
      return api.auth.signUp(firstName, lastName, email)
    },
    async login(email, password) {
      const response = await api.auth.login(email, password)
      if (response?.token) {
        this.token = response.token
      }
      return response
    },
    newPassword(verificationCode, password, confirmPassword) {
      return api.auth.newPassword(verificationCode, password, confirmPassword)
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
      if (response?.user) {
        this.user = response.user
      }
      return response
    },
  },
})
