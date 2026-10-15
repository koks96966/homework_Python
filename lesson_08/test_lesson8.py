import uuid


# POST /api-v2/projects

class TestCreateProject:

    def test_create_project_positive(self, api, unique_title):
        """Позитивный: создание проекта с валидным названием."""
        response = api.create_project(unique_title)

        assert response.status_code == 201, response.text
        body = response.json()
        assert "id" in body and body["id"]
        assert isinstance(body["id"], str)

    def test_create_project_negative_empty_title(self, api):
        """Негативный: пустое поле title должно вернуть ошибку."""
        response = api.create_project("")

        assert response.status_code in (400, 422), response.text
        assert response.text  # непустое тело с описанием ошибки


# PUT /api-v2/projects/{id}

class TestUpdateProject:

    def test_update_project_positive(self, api, created_project):
        """Позитивный: изменение названия существующего проекта."""
        new_title = f"renamed-{uuid.uuid4().hex[:6]}"

    # 1) PUT — проверяем, что запрос принят
        response = api.update_project(created_project, title=new_title)
        assert response.status_code == 200, response.text
        assert response.json().get("id") == created_project

    # 2) GET — проверяем, что изменение реально применилось
        check = api.get_project(created_project)
        assert check.status_code == 200, check.text
        assert check.json().get("title") == new_title

    def test_update_project_negative_unknown_id(self, api):
        """Негативный: обновление несуществующего проекта."""
        fake_id = str(uuid.uuid4())
        response = api.update_project(fake_id, title="whatever")

        # API возвращает 404 (или 400) для несуществующего ресурса
        assert response.status_code in (400, 404), response.text
        assert response.text


# GET /api-v2/projects/{id}

class TestGetProject:

    def test_get_project_positive(self, api, created_project, unique_title):
        """Позитивный: получение существующего проекта."""
        response = api.get_project(created_project)

        assert response.status_code == 200, response.text
        body = response.json()
        assert body.get("id") == created_project
        assert body.get("title") == unique_title

    def test_get_project_negative_unknown_id(self, api):
        """Негативный: получение несуществующего проекта."""
        fake_id = str(uuid.uuid4())
        response = api.get_project(fake_id)

        assert response.status_code in (400, 404), response.text
        assert response.text
