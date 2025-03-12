<script setup>
import { reactive } from 'vue';

const form = reactive({
  verificationCode: "",
  password: "",
  confirmPassword: ""
})

</script>
<template>
  <q-page padding>
    <Container>
      <div>
        <form @submit="">
          <q-input v-model="form.password" label="Password" />
          <q-input v-model="form.confirmPassword" label="Confirm Password" />

          <div class="q-mt-md">
            <q-btn color="positive" type="submit">Create New Password</q-btn>
          </div>

        </form>
      </div>
    </Container>
  </q-page>
</template>
