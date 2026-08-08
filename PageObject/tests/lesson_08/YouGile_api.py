import requests


class YougileAPI:
    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title, description=None, users=None):
        """
        Создание проекта
        Обязательное поле: title
        """
        data = {"title": title}
        if description:
            data["description"] = description
        if users:
            data["users"] = users

        response = requests.post(
            f"{self.url}/api-v2/projects",
            json=data,
            headers=self.headers
        )
        return response

    def update_project(self, project_id, title, description=None, users=None, archived=None):
        """
        Обновление проекта по ID
        Обязательное поле: title
        """
        data = {"title": title}
        if description is not None:
            data["description"] = description
        if users is not None:
            data["users"] = users
        if archived is not None:
            data["archived"] = archived

        response = requests.put(
            f"{self.url}/api-v2/projects/{project_id}",
            json=data,
            headers=self.headers
        )
        return response

    def get_project(self, project_id):
        """
        Получение проекта по ID
        """
        response = requests.get(
            f"{self.url}/api-v2/projects/{project_id}",
            headers=self.headers
        )
        return response

    def get_projects(self, limit=100, offset=0):
        """
        Получение списка проектов
        """
        params = {"limit": limit, "offset": offset}
        response = requests.get(
            f"{self.url}/api-v2/projects",
            headers=self.headers,
            params=params
        )
        return response
