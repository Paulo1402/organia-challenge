import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

import { fileURLToPath, URL } from "node:url";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  define: {
    "process.env": {
      BACKEND_BASE_URL: "http://localhost:8000/api/v1",
    },
  },

  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
    extensions: [".js", ".json", ".jsx", ".mjs", ".ts", ".tsx", ".vue"],
  },
});
