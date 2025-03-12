<script setup>
import { reactive } from 'vue';

const form = reactive({
  email: "",
  password: ""
})

</script>
<template>
  <q-page padding>
    <Container>
      <div>
        <form @submit="">
          <q-input v-model="form.email" label="Email" />
          <q-input v-model="form.password" label="Password" />

          <div class="q-mt-md">
            <q-btn class="q-ml-sm" color="positive" type="submit">Sign In</q-btn>
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
