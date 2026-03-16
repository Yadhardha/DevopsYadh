FROM splunk/splunk:latest

USER root


RUN mkdir -p /logs && chmod 777 /logs

# Copy log generator
COPY log_generator.py /opt/splunk/log_generator.py
RUN chmod +x /opt/splunk/log_generator.py

EXPOSE 8000 9000

# Start Splunk + log generator automatically
CMD ["/sbin/entrypoint.sh start-service"]
