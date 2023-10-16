# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /detect_shape
WORKDIR /detect_shape

# Copy the current directory contents into the container at /detect_shape
COPY . /detect_shape

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "wsgi:app"]
