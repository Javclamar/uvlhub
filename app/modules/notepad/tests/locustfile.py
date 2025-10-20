from locust import HttpUser, TaskSet, task, between
from core.environment.host import get_host_for_locust_testing


class NotepadBehavior(TaskSet):
    
    @task(1)
    def load_list(self):
        print("Cargando lista de notepads")
        response = self.client.get("/notepad")

        if response.status_code != 200:
            print(f"Notepad index failed: {response.status_code}")

    @task(2)
    def create_notepad(self):
        print("Creando un nuevo notepad")
        response = self.client.post("/notepad/create", json={"title": "Notepad locust", "body": "Body locust"})
        if response.status_code != 200:
            print(f"Notepad creation failed: {response.status_code}")

class NotepadUser(HttpUser):
    wait_time = between(1, 5)
    tasks = [NotepadBehavior]
    host = get_host_for_locust_testing()
