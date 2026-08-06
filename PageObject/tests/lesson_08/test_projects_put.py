class TestProjectsPut:

    # ========== ПОЗИТИВНЫЕ ТЕСТЫ ==========

    def test_update_project_success(self, api, created_project):
        """Позитивный тест: обновление проекта"""
        project_id = created_project
        new_title = "Updated Title"

        response = api.update_project(project_id, new_title)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        get_response = api.get_project(project_id)
        assert get_response.status_code == 200
        data = get_response.json()
        assert data["title"] == new_title

    def test_update_project_only_title(self, api, created_project):
        """Позитивный тест: обновление только title"""
        project_id = created_project
        new_title = "Only Title Updated"

        response = api.update_project(project_id, new_title)

        assert response.status_code == 200

        get_response = api.get_project(project_id)
        assert get_response.status_code == 200
        data = get_response.json()
        assert data["title"] == new_title

    # ========== НЕГАТИВНЫЕ ТЕСТЫ ==========

    def test_update_nonexistent_project(self, api):
        """Негативный тест: обновление несуществующего проекта"""
        fake_id = "non-existent-id-12345"
        response = api.update_project(fake_id, "New Title")

        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    def test_update_project_without_title(self, api, created_project):
        """Негативный тест: обновление проекта без title"""
        project_id = created_project
        response = api.update_project(project_id, "")

        assert response.status_code == 400

    def test_update_project_with_invalid_id(self, api):
        """Негативный тест: обновление с невалидным ID"""
        invalid_id = "!@#$%^&*()"
        response = api.update_project(invalid_id, "New Title")

        assert response.status_code in [400, 404]
