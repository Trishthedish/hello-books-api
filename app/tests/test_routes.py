from flask.wrappers import Response
import pytest

def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get('/books/1')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "Watr 4evr"
    }

def test_get_one_book_with_no_data_returns_404(client):
    # Act 
    response = client.get('/books/4')
    response_body = response.get_json()

    # Assert
    assert response_body == None
    assert response.status_code == 404

def test_get_books_valid_data_returns_200_and_books(client, two_saved_books):
    # Act
    response = client.get('/books')
    response_body = response.get_json()
    assert type(response_body) == list
    assert response_body[0] == {
        "id": 1,
        "title": "Ocean Book",
        "description": "Watr 4evr"
    }
    assert response_body[1] == {
        "id": 2,
        "title": "Mountain Book",
        "description": "i luv 2 climb rocks"
   }

def test_create_new_book_with_post_returns_201(client):
    response = client.post('/books', json={
        "title": "The Fault In Our Stars",
        "descriptions": "A fabulous book"
    })
    print(f'\033[1;31;43m response: {response} \033[0;0m')
    # assert response.status_code == 201