FROM splunk/splunk:latest

USER root

# Directories
RUN mkdir -p /tmp/.ansible/tmp && chmod 777 /tmp/.ansible/tmp
RUN mkdir -p /logs && chmod 777 /logs

# Copy log generator
COPY log_generator.py /opt/splunk/log_generator.py
RUN chmod +x /opt/splunk/log_generator.py

EXPOSE 8000 9000

# Start Splunk + log generator automatically
CMD ["/bin/bash","-c","/opt/splunk/bin/python3 /opt/splunk/log_generator.py & /sbin/entrypoint.sh start-service"]
