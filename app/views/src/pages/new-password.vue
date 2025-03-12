<script setup>
import { reactive } from 'vue';
import { useRoute, useRouter } from "vue-router";
import { useAuthStore } from "../store";

const store = useAuthStore()
const route = useRoute()
const router = useRouter()

const form = reactive({
  verificationCode: route.params.token,
  password: "",
  confirmPassword: "",
  isError: false,
})

const onSubmit = () => {
  store.newPassword(form.verificationCode, form.password, form.confirmPassword).then((data) => {
    if (data.message === "new password set!") {
      router.push("/sign-in")
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
        <form @submit="onSubmit">
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
