FROM python:3.10-bullseye

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Run Django's collectstatic command to gather static files
# in a single location that can easily be served by a web server
RUN chmod +x /app/entrypoint.prod.sh
# Run the Django application
CMD ["entrypoint.prod.sh"]