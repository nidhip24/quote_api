from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Quotes API"}


def test_get_all_quotes():
    response = client.get("/quotes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_random_quote():
    response = client.get("/quotes/random")
    if len(response.json()) > 0:
        assert response.status_code == 200
        assert "text" in response.json()
        assert "author" in response.json()
    else:
        assert response.status_code == 404


def test_search_quotes_by_author():
    response = client.get("/quotes/search?author=Einstein")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        quotes = response.json()
        assert all("Einstein" in quote["author"] for quote in quotes)


def test_search_quotes_by_keyword():
    response = client.get("/quotes/search?keyword=life")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        quotes = response.json()
        assert all("life" in quote["text"].lower() for quote in quotes)


def test_search_quotes_not_found():
    response = client.get("/quotes/search?author=NonExistentAuthor123")
    assert response.status_code == 404
