from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "TaskFlow API is running"
    }

def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Test task",
            "description": "Created by pytest",
            "completed": False
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Test task"
    assert data["description"] == "Created by pytest"
    assert data["completed"] is False
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data

def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)    

def test_get_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Get test",
            "description": "Testing GET",
            "completed": False
        }
    )

    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id
    assert response.json()["title"] == "Get test"

def test_update_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Before update",
            "description": "Old description",
            "completed": False
        }
    )

    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "After update",
            "description": "New description",
            "completed": True
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "After update"
    assert data["description"] == "New description"
    assert data["completed"] is True
    assert data["id"] == task_id

def test_patch_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Patch test",
            "description": "Original",
            "completed": False
        }
    )

    task_id = create_response.json()["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        json={
            "completed": True
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["completed"] is True
    assert data["title"] == "Patch test"
    assert data["description"] == "Original"
    assert data["id"] == task_id    


def test_delete_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Delete test",
            "description": "Will be deleted",
            "completed": False
        }
    )

    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id

    get_response = client.get(f"/tasks/{task_id}")

    assert get_response.status_code == 404    