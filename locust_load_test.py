import random
from locust import HttpUser, task, between

class LoadTestClientRegister(HttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = between(1, 2)  # Simulate a user waiting 1-2 seconds between tasks

    @task
    def client_registeration(self):
        data = {
            "fullName": f"TestUser{random.randint(1, 1000)}",
            "userName": f"user{random.randint(1, 1000)}",
            "email": f"user{random.randint(1, 1000)}@example.com",
            "password": f"Password{random.randint(1000, 9999)}",
            "phone": f"987654{random.randint(1000, 9999)}"
        }
        self.client.post("/client_registeration", data=data)
