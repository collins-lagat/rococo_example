<script setup>
import { ref, computed } from 'vue';
import { useAccountStore } from "../store"
import { useRouter } from 'vue-router';

const store = useAccountStore()
const router = useRouter()

const isLoading = ref(true)

const title = computed(() => {
  if (isLoading.value) {
    return "Loading..."
  }
  return `Hi, ${store.user.first_name} ${store.user.last_name}!`
})

store.get().then(() => {
  isLoading.value = false
}).catch(e => {
  if (e.message === "Unauthorized") {
    router.push("/sign-in")
  }
})

</script>
<template>
  <q-page padding>
    <Container>
      <q-card flat bordered class="q-mb-sm cursor-pointer">
        <q-card-section class="q-pt-xs">
          <div class="text-h5 q-mt-sm q-mb-xs">{{ title }}</div>
        </q-card-section>
      </q-card>
    </Container>
  </q-page>
</template>
