# Base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Expose the port your app runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]
