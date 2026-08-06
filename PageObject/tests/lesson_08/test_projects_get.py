class TestProjectsGet:

    # ========== ПОЗИТИВНЫЙ ТЕСТ ==========

    def test_get_project_success(self, api, created_project):
        """Позитивный тест: получение существующего проекта"""
        project_id = created_project

        response = api.get_project(project_id)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert data["id"] == project_id
        assert "title" in data

    # ========== НЕГАТИВНЫЕ ТЕСТЫ ==========

    def test_get_nonexistent_project(self, api):
        """Негативный тест: получение несуществующего проекта"""
        fake_id = "fake-id-12345"
        response = api.get_project(fake_id)

        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    def test_get_project_with_invalid_id(self, api):
        """Негативный тест: получение с невалидным ID"""
        invalid_id = "invalid@id"
        response = api.get_project(invalid_id)

        assert response.status_code in [400, 404]
