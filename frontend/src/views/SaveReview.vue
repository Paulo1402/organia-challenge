<template>
  <v-container class="text-center">
    <h1 class="mb-4">
      {{ mode == "new" ? "Criar avaliação" : "Atualizar avaliação" }}
    </h1>


    <v-form v-model="form" @submit.prevent="saveReview">
      <v-alert
        v-model="showError"
        closable
        type="error"
        text="Algo deu errado ao salvar a avaliação"
      >
      </v-alert>

      <v-text-field
        v-model="reviewer"
        label="Avaliador"
        class="mb-4"
        :rules="[(v) => !!v || 'O nome do avaliador é obrigatório']"
      ></v-text-field>

      <v-date-input
        v-model="reviewDate"
        label="Data de avaliação"
        prepend-icon=""
        class="mb-4"
        :rules="[
          (v) => !!v || 'A data da avaliação é obrigatória',
          (v) => dayjs(v).isValid() || 'Data inválida',
        ]"
      >
      </v-date-input>

      <v-textarea
        v-model="reviewComment"
        label="Avaliação"
        class="mb-4"
        required
        :rules="[(v) => !!v || 'A comentário da avaliação é obrigatório']"
      ></v-textarea>

      <v-select
        label="Modelos para classificação"
        no-data-text="Sem modelos para classificação"
        class="mb-4"
        :items="classifiers"
        :rules="[(v) => !!v || 'Selecione um modelo para classificação']"
      >
      </v-select>

      <v-btn type="submit" color="success" :disabled="!form" :loading="loading">
        {{ mode == "new" ? "Criar avaliação" : "Atualizar avaliação" }}
      </v-btn>
    </v-form>
  </v-container>
</template>

<script setup lang="ts">
import { watch, ref } from "vue"
import { useRoute, useRouter } from "vue-router"
import dayjs from "dayjs"

import reviewsService from "@/services/reviews"

const reviewer = ref("")
const reviewDate = ref<Date>()
const reviewComment = ref("")

const classifiers = ref<string[]>([])

const form = ref(false)
const loading = ref(false)
const showError = ref(false)

const router = useRouter()
const route = useRoute()

const mode = ref(route.name === "new-review" ? "new" : "edit")

if (mode.value === "edit") {
  const reviewId = route.params.id as string

  reviewsService.getReview(reviewId).then((review) => {
    reviewer.value = review.reviewer
    reviewDate.value = review.review_date
    reviewComment.value = review.review_comment
  })
}

watch(
  () => route.name,
  (newVal) => {
    if (newVal === "new-review") {
      mode.value = "new"
    } else {
      mode.value = "edit"
    }
  }
)

reviewsService
  .getReviewClassifiers()
  .then((data) => {
    classifiers.value = data
  })
  .catch((error) => {
    console.error(error)
  })

async function saveReview() {
  const reviewDateFormated = dayjs(reviewDate.value).format("YYYY-MM-DD")

  const review = {
    reviewer: reviewer.value,
    review_date: reviewDateFormated,
    review_comment: reviewComment.value,
  }

  loading.value = true
  showError.value = false

  try {
    if (mode.value === "new") {
      await reviewsService.createReview(review)
    } else {
      const reviewId = route.params.id as string
      await reviewsService.updateReview(reviewId, review)
    }

    loading.value = false
    router.push("/reviews")
  } catch (error) {
    loading.value = false
    showError.value = true

    console.error(error)
  }
}
</script>
