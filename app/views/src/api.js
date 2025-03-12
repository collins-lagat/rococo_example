const API_URL = 'http://localhost:5000/api'

export default {
  auth: {
    async signUp(firstName, lastName, email) {
      try {
        const response = await fetch(`${API_URL}/register`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            firstName,
            lastName,
            email,
          }),
        })
        return await response.json()
      } catch (error) {
        console.error(error)
      }
    },
    async login(email, password) {
      try {
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
        return await response.json()
      } catch (error) {
        console.error(error)
      }
    },
    async newPassword(verificationCode, password, confirmPassword) {
      try {
        const response = await fetch(`${API_URL}/new-password`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            verificationCode,
            password,
            confirmPassword,
          }),
        })
        return await response.json()
      } catch (error) {
        console.error(error)
      }
    },
  },
  account: {
    async get(token) {
      try {
        const response = await fetch(`${API_URL}/account`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
          },
        })
        return await response.json()
      } catch (error) {
        console.error(error)
      }
    },
  }
}
