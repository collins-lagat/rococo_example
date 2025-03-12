<script setup>
import { reactive } from 'vue';

const user = reactive({
  first_name: "John",
  last_name: "Doe",
})
</script>
<template>
  <q-page padding>
    <Container>
      <q-card flat bordered class="q-mb-sm cursor-pointer">
        <q-card-section class="q-pt-xs">
          <div class="text-h5 q-mt-sm q-mb-xs">{{ `Hi, ${user.first_name} ${user.last_name}!` }}</div>
        </q-card-section>
      </q-card>
    </Container>
  </q-page>
</template>
