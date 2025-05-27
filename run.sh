docker build -t accounxt-ms-auth -f Dockerfile .
docker run -p 8090:8000 --env-file .env accounxt-ms-auth