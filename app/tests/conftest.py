import pytest
from app import create_app
from app import db
from app.models.book import Book

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_books(app):
    # Arrange
    ocean_book = Book(
        title="Ocean Book",
        description="Watr 4evr"
    )
    mountain_book = Book(
        title="Mountain Book",
        description="i luv 2 climb rocks"
    )
    db.session.add_all([ocean_book, mountain_book])
    db.session.commit()

@pytest.fixture
def one_saved_book(app):
    parable_of_the_sower = Book(
        title="Parable of the Sower",
        description="The first book in Octavia Butler's EatherSeed ScFi Series"
    )
    db.session.add(parable_of_the_sower)
    db.session.commit()