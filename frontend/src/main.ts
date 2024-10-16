import { createApp } from "vue"

import { createVuetify } from "vuetify"
import * as components from "vuetify/components"
import * as directives from "vuetify/directives"

import "@fortawesome/fontawesome-free/css/all.css" // Ensure your project is capable of handling css files
import { aliases, fa } from "vuetify/iconsets/fa"

import "./style.css"
import App from "./App.vue"
import { VDateInput } from 'vuetify/labs/VDateInput'

import "vuetify/styles"

const vuetify = createVuetify({
  components: {
    ...components,
    VDateInput
  },
  directives,
  icons: {
    defaultSet: "fa",
    aliases,
    sets: {
      fa,
    },
  },
  theme: {
    defaultTheme: "dark",
  },
})

import router from "./router"

createApp(App).use(vuetify).use(router).mount("#app")
