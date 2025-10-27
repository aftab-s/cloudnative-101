# Use an official Nginx image to serve static content
FROM nginx:alpine

# Set working directory
WORKDIR /usr/share/nginx/html

# Remove default nginx static assets
RUN rm -rf ./*

# Copy static website files to nginx html directory
COPY index.html ./
COPY style.css ./
COPY assets ./assets

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
