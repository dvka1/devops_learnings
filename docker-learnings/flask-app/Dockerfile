# Use official lightweight Python image
FROM python:3.9-slim

# Set workdir inside container
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Run Flask app
CMD ["python", "app.py"]

