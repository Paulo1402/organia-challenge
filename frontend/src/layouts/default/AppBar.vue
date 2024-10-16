<template>
  <v-navigation-drawer v-model="drawer" disable-route-watcher>
    <v-list>
      <v-list-subheader>Menu</v-list-subheader>

      <v-list-item exact nav prepend-icon="fa fa-home" to="/">Home</v-list-item>
      <v-list-item exact nav prepend-icon="fa-solid fa-list" to="/reviews"
        >Ver Avaliações</v-list-item
      >
      <v-list-item exact nav prepend-icon="fa-solid fa-plus" @click="handleClick"
        >Nova Avaliação</v-list-item
      >
    </v-list>
  </v-navigation-drawer>

  <v-app-bar>
    <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

    <v-app-bar-title>
      <v-btn :ripple="false" variant="plain" to="/reviews">OrganIA Challenge</v-btn>
    </v-app-bar-title>

    <v-btn class="mr-2" prepend-icon="mdi-circle-slice-4" @click="toggleTheme">
      <template #default>
        <div class="d-none d-sm-flex">Mudar Tema</div>
      </template>
    </v-btn>
  </v-app-bar>
</template>

<script lang="ts" setup>
import { ref } from "vue"
import { useTheme } from "vuetify"
import { useRouter } from "vue-router"

const drawer = ref(false)
const theme = useTheme()

const route = useRouter()

function toggleTheme() {
  theme.global.name.value = theme.global.current.value.dark ? "light" : "dark"
}

function handleClick() {
  console.log('click')
  route.push("/reviews/new")
}
</script>
