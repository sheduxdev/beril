FROM node:latest
WORKDIR /app
COPY . .
RUN npm install --production
ENV API_KEY=AIzaSyA1234567890abcdefghijklmnopqrstuv
EXPOSE 3000
CMD ["node", "server.js"]
