const API_URL = 'http://localhost:5000/api'

export default {
  auth: {
    async signUp(firstName, lastName, email) {
      const response = await fetch(`${API_URL}/register`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          first_name: firstName,
          last_name: lastName,
          email,
        }),
      })
      return response
    },
    async login(email, password) {
      const response = await fetch(`${API_URL}/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email,
          password,
        }),
      })
      return response
    },
    async newPassword(verificationCode, password, confirmPassword) {
      const response = await fetch(`${API_URL}/new-password`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          token: verificationCode,
          password,
          confirm_password: confirmPassword,
        }),
      })
      return response
    },
  },
  account: {
    async get(token) {
      const response = await fetch(`${API_URL}/account`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${token}`,
        },
      })
      return response
    },
  }
}
