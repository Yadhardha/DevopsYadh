FROM ubuntu:22.04

RUN apt update && apt install -y python3 python3-pip curl

COPY app.py /app/app.py

CMD ["python3","/app/app.py"]
