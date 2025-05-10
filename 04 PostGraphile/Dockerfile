FROM node:22-alpine

WORKDIR /app

# Install dependencies (including PostGraphile)
#RUN npm install -g postgraphile

# Copy your package.json and package-lock.json (if applicable)
COPY . .

# Install project dependencies (if any) - skip if you're only running postgraphile
# RUN npm install

# Set the working directory
WORKDIR /app