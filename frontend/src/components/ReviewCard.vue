<template>
    <v-card max-width="600" class="d-flex flex-column mx-auto">
        <v-card-title>{{ review.reviewer }}</v-card-title>
        <v-card-text class="flex-grow-1">{{ review.review_comment }}</v-card-text>

        <v-spacer />
        <v-card-actions>
            <v-spacer />
            <v-btn color="primary" :to="'reviews/' + review.id">Editar</v-btn>
            <v-btn color="error" :loading="loading">
                <v-dialog v-model="dialog" activator="parent" width="auto">
                    <v-card title="ATENÇÃO">
                        <v-card-text>Deseja deletar essa avaliação?</v-card-text>

                        <v-card-actions>
                            <v-spacer />
                            <v-btn @click="handleDelete" color="error">Sim</v-btn>
                            <v-btn @click="dialog = false">Cancelar</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>Deletar
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script setup lang="ts">
import { ref } from "vue"

import reviewsService from "@/services/reviews"

const dialog = ref(false)
const loading = ref(false)

const props = defineProps<{
    review: {
        id: number;
        reviewer: string;
        review_comment: string;
    }
}>()

function handleDelete() {
    loading.value = true

    reviewsService.deleteReview(props.review.id).then(() => {
        loading.value = false
        window.location.reload()
    }).catch((error) => {
        console.error(error)
    })
}
</script>