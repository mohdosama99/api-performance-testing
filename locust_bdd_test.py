import random
from locust import HttpUser, task, between

class BDDLoadTest(HttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = between(1, 3)  # Wait 1-3 seconds between tasks to simulate real user behavior

    @task
    def bdd_load_test(self):
        # Randomly select an endpoint to test
        if random.choice([True, False]):
            # Test /client_registeration
            data = {
                "fullName": f"TestUser{random.randint(1, 1000)}",
                "userName": f"user{random.randint(1, 1000)}",
                "email": f"user{random.randint(1, 1000)}@example.com",
                "password": f"Password{random.randint(1000, 9999)}",
                "phone": f"987654{random.randint(1000, 9999)}"
            }
            self.client.post("/client_registeration", data=data)
        else:
            # Test /client_login
            data = {
                "userName": f"user{random.randint(1, 1000)}",
                "email": f"user{random.randint(1, 1000)}@example.com",
                "password": f"Password{random.randint(1000, 9999)}"
            }
            self.client.post("/client_login", data=data)
