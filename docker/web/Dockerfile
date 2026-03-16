FROM ubuntu:22.04

RUN apt-get update && apt-get install -y nginx python3 python3-pip && rm-rf /var/lib/apt/lists/*

RUN mkdir -p /tmp/.ansible/tmp && chmpd 777 /tmp/.ansible/tmp

RUN mkdir -p /var/www/html
COPY index.html /var/www/html/index.html
RUN chmod 644 /var/www/html/index.html

EXPOSE 8080

CMD["nginx","-g","daemon off;"]
