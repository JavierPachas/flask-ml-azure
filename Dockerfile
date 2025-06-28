# Use official Python 3.8 slim image as the base
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Expose the port your Flask app runs on
EXPOSE 5002

# Command to run the Flask app
CMD ["python", "app.py"]
