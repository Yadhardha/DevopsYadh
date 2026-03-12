FROM nginx:latest

RUN apt update && apt install -y python3 python3-pip curl

COPY index.html /var/www/html/index.html

EXPOSE 80
