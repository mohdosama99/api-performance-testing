import random
from locust import HttpUser, task, between

class StressTestClientLogin(HttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = between(0.5, 1)  # Simulate high-frequency requests

    @task
    def client_login(self):
        data = {
            "userName": "test99",  # Using a predefined valid user
            "email": "testaut@xyz.com",
            "password": "Test@123"
        }
        self.client.post("/client_login", data=data)
