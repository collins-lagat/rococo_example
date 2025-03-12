<script setup>
import { reactive } from 'vue';

const form = reactive({
  firstName: "",
  lastName: "",
  email: ""
})

</script>
<template>
  <q-page padding>
    <Container>
      <div>
        <form @submit="">
          <q-input v-model="form.firstName" label="First Name" />
          <q-input v-model="form.lastName" label="Last Name" />
          <q-input v-model="form.email" label="Email" />

          <div class="q-mt-md">
            <q-btn class="q-ml-sm" color="positive" type="submit">Sign Up</q-btn>
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
