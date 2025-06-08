# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy only what’s needed
COPY worker.py /app/worker.py
COPY requirements.txt /app/requirements.txt

# Install any dependencies (if you have more, list them in requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Expose port if your worker needs to receive HTTP (optional)
# EXPOSE 1234

# Default command to run your script
CMD ["python", "worker.py"]