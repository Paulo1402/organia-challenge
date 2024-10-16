<template>
  <v-container class="text-center">
    <!-- 
        <v-carousel hide-delimiter-background show-arrows="hover">
            <v-carousel-item v-for="review in reviews" :key="review.id">
                <review-card :review="review" />
            </v-carousel-item>
        </v-carousel> -->

    <div v-if="reviews.length > 0">
      <h1 class="mb-8">Avaliações</h1>

      <v-row v-for="review in reviews" :key="review.id" cols="12" md="4">
        <v-col>
          <review-card :review="review" />
        </v-col>
      </v-row>
    </div>
    <div v-else>
      <h1 class="mb-4">
        Parece que não há nenhuma avaliação ainda... Crie um agora!
      </h1>
      <v-btn color="success" to="/reviews/new">Criar avaliação</v-btn>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from "vue"

import ReviewCard from "@/components/ReviewCard.vue"
import reviewsService from "@/services/reviews"

const reviews = ref<any[]>([])

reviewsService.getReviews().then((data) => {
  reviews.value = data
}).catch((error) => {
  console.error(error)
})
</script>
