FROM node:latest

WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
EXPOSE 8080
CMD ["npm", "start"]

#docker build -t express-app .
#docker container run -p 8080:8080 express-app  