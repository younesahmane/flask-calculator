Project Documentation for the Flask Web-Based Calculator


1. Project Overview
    The Flask-based web calculator is designed to perform basic arithmetic operations (addition, subtraction, multiplication, and division) via a web-based API. Users can access the calculator by making HTTP GET requests to specific endpoints with two real numbers. The result of the operation will be returned in JSON format.


2. Technologies Used
    Backend Framework: Flask (Python)
    Development Environment: Python 3.8+
    Libraries:
    Flask: Web framework for developing the API.
    JSON: Used for formatting API responses.


3. API Design
    The calculator exposes four endpoints, each corresponding to a specific mathematical operation:

    Addition Endpoint:
        URL: /add/<numberA>/<numberB>
        Method: GET
        Example: /add/1/3
        Response:
            *JSON CODE*
            {
            "status": 200,
            "result": 4
            }
            *JSON CODE*

    Subtraction Endpoint:
        URL: /minus/<numberA>/<numberB>
        Method: GET
        Example: /minus/6/3
        Response:
            *JSON CODE*
            {
            "status": 200,
            "result": 3
            }
            *JSON CODE*

    Multiplication Endpoint:
        URL: /multiply/<numberA>/<numberB>
        Method: GET
        Example: /multiply/6/3
        Response:
            *JSON CODE*
            {
            "status": 200,
            "result": 18
            }
            *JSON CODE*

    Division Endpoint:
        URL: /divide/<numberA>/<numberB>
        Method: GET
        Example: /divide/6/3
        Response:
            *JSON CODE*
            {
            "status": 200,
            "result": 2
            }
            *JSON CODE*


4. Error Handling
    If an operation involves division by zero, the API returns an appropriate error message:
        *JSON CODE*
        {
        "status": 400,
        "error": "Division by zero is not allowed"
        }
        *JSON CODE*
    If non-numeric input is provided, the API will return a validation error:
        *JSON CODE*
        {
        "status": 400,
        "error": "Invalid input"
        }
        *JSON CODE*


5. Setup and Installation
Prerequisites:
    Python 3.8+
    Flask installed (pip install flask)

Project Setup:
    Create a new directory for the project and navigate to it.
    Create a virtual environment and activate it:

    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows

Install Flask:
    pip install flask
    Create a Python file (app.py) and implement the Flask endpoints as described.

Run the Application:
    To start the Flask server, run the following command in your terminal:
    flask run

Accessing the API:
    The API will be available at http://127.0.0.1:5000.
    Test the calculator by making HTTP requests to the appropriate endpoints (e.g., using a browser or a tool like Postman)