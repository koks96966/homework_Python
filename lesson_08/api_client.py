import requests
from config import BASE_URL


class YouGileApi:

    def __init__(self, token: str, base_url: str = BASE_URL):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def create_project(self, title: str, users: dict | None = None):
        payload = {"title": title}
        if users is not None:
            payload["users"] = users
        return self.session.post(f"{self.base_url}/projects", json=payload)

    def update_project(self, project_id: str, **fields):
        return self.session.put(
            f"{self.base_url}/projects/{project_id}", json=fields
        )

    def get_project(self, project_id: str):
        return self.session.get(f"{self.base_url}/projects/{project_id}")

    def delete_project(self, project_id: str):
        return self.session.delete(f"{self.base_url}/projects/{project_id}")
