import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  root: __dirname, // Explicitly set the root directory
  publicDir: 'public', // Ensure the public directory is correctly configured
  plugins: [react()],
  server: {
    open: true,
    host: true, // Expose the server to external connections
    proxy: {
      '/api': {
        target: 'http://localhost:8000', // Backend server
        changeOrigin: true,
        secure: false,
      },
    },
  },
  build: {
    outDir: 'build',
  },
  define: {
    'process.env': {}, // Define process.env to avoid undefined errors
  },
});
