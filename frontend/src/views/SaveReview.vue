<template>
  <v-container class="text-center">
    <h1 class="mb-4">
      {{ mode == "new" ? "Criar avaliação" : "Atualizar avaliação" }}
    </h1>

    <v-form @submit.prevent="saveReview">
      <v-text-field
        v-model="reviewer"
        label="Avaliador"
        class="mb-2"
      ></v-text-field>
      <v-text-field
        v-model="reviewDate"
        label="Data de avaliação"
        class="mb-2"
      ></v-text-field>
      <v-textarea
        v-model="reviewComment"
        label="Avaliação"
        class="mb-2"
      ></v-textarea>

      <v-combobox label="Modelos para classificação" :items="classifiers">
      </v-combobox>
    </v-form>
  </v-container>
</template>

<script setup lang="ts">
import { watch, ref } from "vue"
import { useRoute } from "vue-router"

import reviewService from "@/services/reviews"

const reviewer = ref("")
const reviewDate = ref("")
const reviewComment = ref("")
const classifiers = ref<string[]>([])

const route = useRoute()
const mode = ref(route.name === "new-review" ? "new" : "edit")

if (mode.value === "edit") {
  const reviewId = route.params.id as string

  reviewService.getReview(reviewId).then((review) => {
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

reviewService.getReviewClassifiers().then((data) => {
  classifiers.value = data
}).catch((error) => {
  console.error(error)
})

function saveReview() {

}

</script>
