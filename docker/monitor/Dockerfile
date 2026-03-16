FROM splunk/splunk:latest
 
# Install Python inside the container
USER root
RUN apt-get update && apt-get install -y python3 python3-pip
 
# Set up /tmp
RUN mkdir -p /tmp/ansible-tmp && chmod 777 /tmp/ansible-tmp
 
# Copy log generator
COPY log_generator.py /opt/splunk/log_generator.py
RUN chmod +x /opt/splunk/log_generator.py
 
EXPOSE 8000 8080