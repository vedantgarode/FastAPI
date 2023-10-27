# Use an official Python runtime as a parent image
FROM python:3.9


WORKDIR /app

COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variables
ENV FASTAPI_HOST 0.0.0.0
ENV FASTAPI_PORT 80

# Run app.py when the container launches
CMD ["hypercorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
