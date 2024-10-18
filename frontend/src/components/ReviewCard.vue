<template>
  <v-card max-width="600" class="d-flex flex-column mx-auto">
    <v-card-title
      >{{ review.reviewer }} - {{ review.review_date }}</v-card-title
    >
    <v-card-text class="flex-grow-1">{{ review.review_comment }}</v-card-text>

    <v-divider class="my-4" />

    <v-card-subtitle>
      <p>Classificação da avaliação: {{ review.review_classification }}</p>
      <v-divider vertical></v-divider>
      <p>Modelo de classificação: {{ review.review_classifier }}</p>
    </v-card-subtitle>

    <v-card-actions>
      <v-spacer />
      <v-btn color="primary" :to="'reviews/' + review.id">Editar</v-btn>
      <v-btn color="error">
        <v-dialog v-model="dialog" activator="parent" width="auto">
          <v-card title="ATENÇÃO">
            <v-card-text>Deseja deletar essa avaliação?</v-card-text>

            <v-card-actions>
              <v-spacer />
              <v-btn @click="handleDelete" color="error" :loading="loading"
                >Sim</v-btn
              >
              <v-btn @click="dialog = false">Cancelar</v-btn>
            </v-card-actions>
          </v-card> </v-dialog
        >Deletar
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup lang="ts">
import { ref } from "vue"

import reviewsService from "@/services/reviews"
import { Review } from "@/services/reviews/types"

const dialog = ref(false)
const loading = ref(false)

const props = defineProps<{
  review: Review
}>()

const emit = defineEmits(["delete"])

function handleDelete() {
  loading.value = true

  reviewsService
    .deleteReview(props.review.id)
    .then(() => {
      emit("delete", props.review.id)
    })
    .catch((error) => {
      console.error(error)
    })
    .finally(() => {
      dialog.value = false
      loading.value = false
    })
}
</script>
