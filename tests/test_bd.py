import pytest
from app import create_app


@pytest.fixture
def app():
    app = create_app(testing=True)
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_db_connection(client):
    # Проверка доступа к базе данных
    response = client.get('/test-db-connection')  # Замените на ваш путь
    assert response.status_code == 200
