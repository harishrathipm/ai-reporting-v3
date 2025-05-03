# Use the official Node.js image as the base image
FROM node:20-slim AS builder

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json (if available) first to leverage Docker caching
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React app
RUN npm run build

# Final stage to reduce image size
FROM node:20-slim
WORKDIR /app
COPY --from=builder /app/build /app/build

# Install serve globally
RUN npm install -g serve

# Expose the port the app runs on
EXPOSE 3000

# Add a health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s CMD curl -f http://localhost:3000 || exit 1

# Use serve to serve the built app
CMD ["serve", "-s", "build", "-l", "3000"]