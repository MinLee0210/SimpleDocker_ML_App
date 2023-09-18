# Use an official Python runtime as a base image
FROM python:3.8-slim
# Set the working directory
WORKDIR /app
# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# Copy the current directory contents into the container at /app
COPY . .
# Expose port 8000 for FastAPI
EXPOSE 8000
# Run main.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]