# Use official Python image as base
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire FastAPI app to the container
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run FastAPI with Uvicorn in production mode
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
