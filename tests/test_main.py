import pytest

from app.main import TASKS, app


@pytest.fixture
def client():
    TASKS.clear()
    return app.test_client()


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_add_and_list_tasks(client):
    resp = client.post("/tasks", json={"title": "Învăț CI/CD"})
    assert resp.status_code == 201
    assert client.get("/tasks").get_json()[0]["title"] == "Învăț CI/CD"


def test_add_task_without_title(client):
    resp = client.post("/tasks", json={})
    assert resp.status_code == 400
