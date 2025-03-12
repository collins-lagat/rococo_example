<script setup>
import { reactive } from 'vue';
import { useAuthStore } from "../store"

const store = useAuthStore()

const form = reactive({
  email: "",
  password: "",
  isError: false,
})

const onSubmit = () => {
  store.login(form.email, form.password).catch((e) => {
    form.isError = true
  })
}

</script>
<template>
  <q-page padding>
    <Container>
      <div>
        <form @submit="onSubmit">
          <q-input v-model="form.email" label="Email" />
          <q-input v-model="form.password" label="Password" />

          <div class="q-mt-md">
            <q-btn class="q-ml-sm" :color="form.isError ? 'negative' : 'positive'" type="submit">Sign In</q-btn>
            <span v-if="form.isError" class="q-ml-sm text-red-10">Invalid email or password</span>
          </div>

          <div class="q-mt-md">
            <span>Don't have an account?</span>
            <q-btn class="q-ml-sm" color="secondary" size="sm" type="a" to="/sign-up" outline>sign up</q-btn>
          </div>
        </form>
      </div>
    </Container>
  </q-page>
</template>
