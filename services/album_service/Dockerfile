# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8000
EXPOSE 8000

# Define the command to run your app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
