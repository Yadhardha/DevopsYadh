FROM splunk/splunk:latest

USER root

RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /tmp/.ansible/tmp && chmod 777 /tmp/.ansible/tmp
RUN mkdir -p /logs && chmod 777 /logs

COPY log_generator.py /opt/splunk/log_generator.py
RUN chmod +x /opt/splunk/log_generator.py

EXPOSE 8000 9000

CMD ["/bin/bash","-c","/opt/splunk/log_generator.py & /sbin/entrypoint.sh start-service"]
