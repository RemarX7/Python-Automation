import os
import pytest
from YouGile_api import YougileAPI


@pytest.fixture
def api():
    BASE_URL = "https://ru.yougile.com"
    TOKEN = os.getenv("YOUGILE_TOKEN", "3hrRDCJadgtFRxL2_GUUo_k8T8ccdLJ37L52r1QcRG61i-9Nbb1rzCtWMwMlBpE8")
    return YougileAPI(BASE_URL, TOKEN)


@pytest.fixture
def created_project(api):
    import time
    title = f"Test Project {int(time.time())}"
    response = api.create_project(title)
    assert response.status_code == 201, f"Failed to create project: {response.json()}"
    project_id = response.json()["id"]
    yield project_id
