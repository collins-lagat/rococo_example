<script setup>
import { reactive } from 'vue';
import { useAuthStore } from "../store"

const store = useAuthStore()

const form = reactive({
  firstName: "",
  lastName: "",
  email: "",
  isError: false,
  isSuccess: false,
})

const onSumbit = () => {
  store.signUp(form.firstName, form.lastName, form.email).then((res) => {
    if (res?.message) {
      form.isSuccess = true
    }
  }).catch((e) => {
    form.isError = true
  })
}

</script>
<template>
  <q-page padding>
    <Container>
      <div>
        <form @submit="onSumbit">
          <q-input v-model="form.firstName" label="First Name" />
          <q-input v-model="form.lastName" label="Last Name" />
          <q-input v-model="form.email" label="Email" />

          <div class="q-mt-md">
            <q-btn class="q-ml-sm" :color="form.isError ? 'negative' : 'positive'" type="submit">Sign Up</q-btn>
            <span v-if="form.isSuccess" class="q-ml-sm text-green-10">Success! Check your email for instructions to
              complete your registration</span>
            <span v-if="form.isError" class="q-ml-sm text-red-10">Invalid email or password</span>
          </div>

          <div class="q-mt-md">
            <span>Already have an account?</span>
            <q-btn class="q-ml-sm" color="secondary" size="sm" type="a" to="/sign-in" outline>Sign In</q-btn>
          </div>
        </form>
      </div>
    </Container>
  </q-page>
</template>
