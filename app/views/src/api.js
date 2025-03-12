const API_URL = 'http://localhost:5000'

export default {
  auth: {
    async signUp(firstName, lastName, email) {
      try {
        const respone = await fetch(`${API_URL}/auth/signup`, {
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
        return await respone.json()
      } catch (error) {
        console.error(error)
      }
    },
    async login(email, password) {
      try {
        const respone = await fetch(`${API_URL}/auth/login`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email,
            password,
          }),
        })
        return await respone.json()
      } catch (error) {
        console.error(error)
      }
    },
    async newPassword(verificationCode, password, confirmPassword) {
      try {
        const respone = await fetch(`${API_URL}/auth/new-password`, {
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
        return await respone.json()
      } catch (error) {
        console.error(error)
      }
    },
  },
  account: {
    async get(token) {
      try {
        const respone = await fetch(`${API_URL}/account`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
          },
        })
        return await respone.json()
      } catch (error) {
        console.error(error)
      }
    },
  }
}
