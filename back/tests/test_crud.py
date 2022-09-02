from back.api.endpoints.crud import router
from fastapi.testclient import TestClient

client = TestClient(router)

def test_get_all():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json()

def test_get_by_title():
    response = client.get("/books/get_book_by_title?keyword=quijote")
    assert response.status_code == 200
    assert response.json() == [
        {
        "id": 1,
        "title": "Don Quijote de la Mancha",
        "author": "Miguel de Cervantes",
        "genre": "Aventuras, caballería",
        "release_year": 1605
        }
    ]  

