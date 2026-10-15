import uuid
import pytest
from config import API_TOKEN
from api_client import YouGileApi


@pytest.fixture(scope="session")
def api():
    if not API_TOKEN:
        pytest.skip(
            "Не задан YOUGILE_TOKEN. Установите переменную окружения."
        )
    return YouGileApi(API_TOKEN)


@pytest.fixture
def unique_title():
    return f"AT-project-{uuid.uuid4().hex[:8]}"


@pytest.fixture
def created_project(api, unique_title):
    """Создаёт проект и удаляет его после теста."""
    response = api.create_project(unique_title)
    assert response.status_code == 201, response.text
    project_id = response.json()["id"]
    yield project_id
    api.delete_project(project_id)
