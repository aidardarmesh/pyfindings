# Use an official Python image as the base
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements file to container
COPY app/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application to the container
COPY app/ /app/

# Expose the port on which FastAPI runs
EXPOSE 8000

# Command to run the application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]