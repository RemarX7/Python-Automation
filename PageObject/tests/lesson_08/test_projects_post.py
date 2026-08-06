import requests


class TestProjectsPost:

    # ========== ПОЗИТИВНЫЙ ТЕСТ ==========

    def test_create_project_success(self, api):
        title = "My New Project"
        response = api.create_project(title)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"

        data = response.json()
        assert "id" in data, "Response should contain 'id'"

        project_id = data["id"]
        get_response = api.get_project(project_id)
        assert get_response.status_code == 200
        project_data = get_response.json()
        assert project_data["title"] == title

    # ========== НЕГАТИВНЫЕ ТЕСТЫ ==========

    def test_create_project_without_title(self, api):
        """Негативный тест: создание проекта без обязательного поля title"""
        response = api.create_project("")

        assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    def test_create_project_with_empty_title(self, api):
        """Негативный тест: создание проекта с пустым title"""
        response = api.create_project("")
        assert response.status_code == 400

    def test_create_project_with_invalid_data(self, api):
        """Негативный тест: создание проекта с невалидными данными"""
        response = requests.post(
            f"{api.url}/api-v2/projects",
            json={"title": 12345},
            headers=api.headers
        )
        assert response.status_code == 400
