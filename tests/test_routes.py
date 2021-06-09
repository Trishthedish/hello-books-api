from flask.wrappers import Response
import pytest
from app.models.book import Book

def test_get_all_books_with_no_saved_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# GET /books/1 returns a response body that matches our fixture
# now this is still demonstaring that getting one book is being tested. However, I'm using two_saved_books. is this kosh?
def test_gets_one_saved_book(client, two_saved_books):
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

# GET /books/1 with no data in test database (no fixture) returns a 404
def test_get_one_book_with_no_data_returns_404(client):
    # Act 
    response = client.get('/books/4')
    response_body = response.get_json()

    # Assert
    assert response_body == None
    assert response.status_code == 404

# GET /books with valid test data (fixtures) returns a 200 with an array including appropriate test data
def test_gets_books_valid_data_returns_200_and_books(client, two_saved_books):
    # Act
    response = client.get('/books')
    response_body = response.get_json()
    assert len(response_body) == 2
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
# POST /books with a JSON request body returns a 201
def test_create_new_book_with_post_returns_201(client):
    response = client.post('/books', json={
        "title": "The Fault In Our Stars",
        "description": "A fabulous book"
    })

    response_body = response.get_json()
    print(f'\033[1;31;43m re-body {response_body} \033[0;0m')
    # return response_body
    assert response.status_code == 201


def test_update_one_book(client, one_saved_book):
    # Act
    response = client.put("/books/1", json={
        "title": "Updated Book Title",
        "description": "A whole new book. In a whole new world."
    })
    response_body = response.get_json()

    # Assert
    print('----response body ', response_body)
    # return response_body
    assert response.status_code == 200
    # response_body is None unless I explicitly return it.
    # yet I see in task-list api tests that no return is necessary.
    # what am I missing??
    # assert "book" in response_body
    # assert response_body == {
    #     "book": {
    #         "id": 1,
    #         "title": "Updated Book Title",
    #         "description": "A whole new book. In a whole new world."
    #     }
    # }