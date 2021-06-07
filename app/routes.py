from app import db
from app.models.book import Book
from flask import request, Blueprint, make_response, jsonify

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET","POST"])
def handle_books():
    if request.method == "GET":

        title_query = request.args.get("title")
        if title_query:
            books = Book.query.filter_by(title=title_query)
        else:
            books = Book.query.all()
        books_response = []
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
        return jsonify(books_response)
    elif request.method == "POST":

        request_body = request.get_json(request.data)
        if not "title" in request_body.keys() or not "description" in request_body.keys():
            return make_response("", 422)
        new_book = Book(
            title=request_body["title"],
            description=request_body["description"]
        )
        db.session.add(new_book)
        db.session.commit()
        return make_response(f"Book {new_book.title} successfully created.", 201)

@books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
def handle_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        return make_response("", 404)

    if request.method == "GET":

        return {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }

    elif request.method == "PUT":

        form_data = request.get_json()
        book.title = form_data["title"]
        book.description = form_data["description"]
        db.session.commit()
        return make_response(f"Book #{book.id} succesfully updated.")

    elif request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return make_response(f"Book #{book.id} successfully deleted.")