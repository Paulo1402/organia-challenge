<template>
  <v-app>
    <AppBar />
    <default-view />
    <AppFooter />
  </v-app>
</template>

<script setup lang="ts">
import AppBar from "./AppBar.vue";
import AppFooter from "./AppFooter.vue";
import DefaultView from "./View.vue";
</script>
