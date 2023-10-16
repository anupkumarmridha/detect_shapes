# Flask App - Local Setup Guide

This repository contains a Flask web application for detecting shapes in a matrix. This README provides instructions on how to download the repository and set up the application on your local machine.

## Prerequisites

Before you begin, ensure you have the following software installed on your local machine:

- [Python 3](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/) (Optional for Docker setup)

## Getting Started

Follow these steps to set up and run the Flask app on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/anupkumarmridha/detect_shapes.git
cd detect_shapes
```

### 2. Virtual Environment (Optional)
It's a good practice to create a virtual environment to isolate project dependencies.

- Create a virtual environment:

```bash
    virtualenv venv
```

- Activate the virtual environment:

  - On Windows:

    ```bash
        venv\Scripts\activate
    ```

  - On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

### 3. Install Dependencies

Install the required Python packages using pip.

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App
Run the Flask app locally.

```bash
python app.py
```
The app will be accessible at http://localhost:5000. You can access the API endpoint at http://localhost:5000/detect_shapes.

### 5. Using Docker (Optional)
If you prefer to use Docker for local development, you can build and run a Docker container.

docker build -t detect_shapes.

#### Build the Docker image:

```bash
docker build -t detect_shapes .
```

#### Run the Docker container:

```bash
docker run -d --name detect-shape-api -p 5000:5000 detect-shapes
```

The app will be accessible at http://localhost:5000.

### 6. Test the App
Use the provided API endpoints to test the Flask app.

**Sample Request**
- For example, you can use tools like curl or Postman to send JSON data to the http://localhost:4000/detect_shapes endpoint.


```json
{
    "matrix": [
        ["G", "M", "N", "B"],
        ["G", "M", "N", "B"],
        ["G", "M", "N", "B"],
        ["G", "M", "N", "B"]
    ]
}
```

**Sample Response**
The Flask app will respond with detected shapes:

```json
{
  "B": {
    "location": [
      "right"
    ],
    "shape": "vertical rectangle"
  },
  "G": {
    "location": [
      "left"
    ],
    "shape": "vertical rectangle"
  },
  "M": {
    "location": [
      "left"
    ],
    "shape": "vertical rectangle"
  },
  "N": {
    "location": [
      "right"
    ],
    "shape": "vertical rectangle"
  }
}
```
