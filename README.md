# api-performance-testing
A performance testing suite for a Flask application. This repository includes scripts for load testing, stress testing, and behavior-driven development (BDD) load testing using Locust.

# Steps to Set Up and Run the Project

# 1. Clone the Repository
# Open your terminal and run:
```bash
git clone git@github.com:mohdosama99/api-performance-testing.git
```

cd flask-api-performance-tests

# 2. Set Up the Flask App
# a) Create a Virtual Environment:
```bash
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

# b) Install Dependencies:
```bash
pip3 install -r requirements.txt
```

# c) Run the Flask App:
```bash
python3 test.py
```
# Comment: The Flask app should now be running at http://127.0.0.1:5000. You can verify by opening the URL in your browser and seeing "Hello, World!"

# 3. Run Performance Tests Using Locust
# Install Locust (if not already installed):
```bash
pip3 install locust
```

# Flask API Performance Testing

This repository contains performance testing scripts for a Flask application. The tests are written using Locust, a Python-based load testing tool. The suite evaluates the following API endpoints:

- `/client_registeration`
- `/client_login`
- `/update_info`
- `/products`

## Features

1. **Load Testing**:
   - Simulates concurrent users accessing the `/client_registeration` endpoint to evaluate its performance under normal conditions.

2. **Stress Testing**:
   - Tests the `/client_login` endpoint under high load to assess its stability and capacity.

3. **BDD Load Testing**:
   - Alternates between `/client_registeration` and `/client_login` endpoints with dynamically generated data for a comprehensive load evaluation.

## Prerequisites

- Python 3.7+
- Locust

### Install Locust
```bash
pip3 install locust
```

## Running the Tests

### 1. Load Testing
Run the load testing script:
```bash
python3 -m locust -f locust_load_test.py --users 100 --spawn-rate 10 --run-time 1m
```

### 2. Stress Testing
Run the stress testing script:
```bash
python3 -m locust -f locust_stress_test.py --users 200 --spawn-rate 20 --run-time 1m
```

### 3. BDD Load Testing
Run the BDD load testing script:
```bash
python3 -m locust -f locust_bdd_test.py --users 100 --spawn-rate 10 --run-time 1m
```

### Access Locust Web UI
Open a browser and go to [http://0.0.0.0:8089](http://0.0.0.0:8089).

- Configure the number of users and spawn rate.
- Monitor performance metrics and export test reports.

## Running Tests in Headless Mode (CI/CD Integration)
To integrate BDD load testing into a CI/CD pipeline, use the headless mode:
```bash
locust -f locust_bdd_test.py --headless -u 10 -r 1 --run-time 5m --csv locust_report
```

## Files in the Repository

1. **locust_load_test.py**:
   - Script for load testing `/client_registeration` endpoint.

2. **locust_stress_test.py**:
   - Script for stress testing `/client_login` endpoint.

3. **locust_bdd_test.py**:
   - Script for BDD load testing of both endpoints.

## Exported Test Results
Test results can be exported as CSV files for analysis. For example:
```bash
locust -f locust_bdd_test.py --headless -u 10 -r 1 --run-time 5m --csv locust_report
```

## Contributing
Feel free to fork this repository and contribute by submitting pull requests.

