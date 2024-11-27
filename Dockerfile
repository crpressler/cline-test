FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script
COPY webpage_monitor.py .

# Create directories for state and changes
RUN mkdir -p /app/state /app/changes

# Create volumes for persistent storage
VOLUME ["/app/state", "/app/changes"]

# Set the entrypoint
ENTRYPOINT ["python", "webpage_monitor.py"]
