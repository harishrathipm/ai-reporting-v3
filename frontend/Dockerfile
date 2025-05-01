# Use the official Node.js image as the base image
FROM node:20-slim

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

# Remove unnecessary files to keep the image lightweight
RUN rm -rf node_modules

# Use serve to serve the built app
CMD ["serve", "-s", "build", "-l", "3000"]