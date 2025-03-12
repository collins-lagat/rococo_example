import { defineStore } from 'pinia';

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
  },
  actions: {
    signUp(firstName, lastName, email) {
      // TODO: Implement sign up logic
    },
    login(email, password) {
      // TODO: Implement login logic
    },
    newPassword(verificationCode, password, confirmPassword) {
      // TODO: Implement new password logic
    },
  },
})
