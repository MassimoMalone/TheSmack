// frontend/vite.config.ts

import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],

  // 👇 Add the server configuration here
  server: {
    // This sets up the proxy
    proxy: {
      // 1. When the frontend requests a path starting with '/api' (e.g., /api/smacks)
      "/api": {
        // 2. Vite redirects that request to your FastAPI server (on port 8000)
        target: "http://127.0.0.1:8000",
        changeOrigin: true, // Rewrites the Host header for the backend
        secure: false, // Necessary for local HTTP connections
      },
    },
  },
});
