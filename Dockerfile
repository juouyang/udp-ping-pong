# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy the server script into the container
COPY src/server_UDP.py /app/

# Expose the default UDP port
EXPOSE 12345/udp

# Set the default entrypoint to run the server
ENTRYPOINT ["python3", "server_UDP.py"]
