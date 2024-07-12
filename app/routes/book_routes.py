from flask import Blueprint, jsonify, request
from app.models import db, Book, Bookorder

book_bp = Blueprint('book_bp', __name__)

# -------------- ROUTES --------------

@book_bp.route('/book', methods=['GET'])
def getBooks():
    books = Book.query.all()
    books_list = []
    for book in books:
        book_data = {
            'isbn': book.isbn,
            'title': book.title,
            'author': {
                'idauthor': book.author.idauthor,
                'firstname': book.author.firstname,
                'lastname': book.author.lastname
            },
            'genre': {
                'idgenre': book.genre.idgenre,
                'name': book.genre.name
            },
            'price': book.price,
            'quantity': book.quantity,
            'language': book.language,
            'editorial': book.editorial,
            'pages': book.pages
        }
        books_list.append(book_data)
    return jsonify(books_list), 200

@book_bp.route('/book/<isbn>', methods=['GET'])
def getBookById(isbn):
    book = Book.query.get(isbn)
    if book:
        book_data = {
            'isbn': book.isbn,
            'title': book.title,
            'author': {
                'idauthor': book.author.idauthor,
                'firstname': book.author.firstname,
                'lastname': book.author.lastname
            },
            'genre': {
                'idgenre': book.genre.idgenre,
                'name': book.genre.name
            },
            'price': book.price,
            'quantity': book.quantity,
            'language': book.language,
            'editorial': book.editorial,
            'pages': book.pages
        }
        return jsonify(book_data), 200
    return jsonify({'message': 'Book not found'}), 404

@book_bp.route('/book', methods=['POST'])
def createBook():
    data = request.get_json()
    new_book = Book(isbn=data['isbn'], title=data['title'], price=data['price'], quantity=data['quantity'],
                    language=data['language'], editorial=data['editorial'], pages=data['pages'],
                    idauthor=data['idauthor'], idgenre=data['idgenre'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'New book created'}), 201

@book_bp.route('/book/<isbn>', methods=['PUT'])
def updateBookById(isbn):
    data = request.get_json()
    book = Book.query.get(isbn)
    if book:
        book.title=data['title']
        book.price=data['price']
        book.quantity=data['quantity']
        book.language=data['language']
        book.editorial=data['editorial']
        book.pages=data['pages']
        book.idauthor=data['idauthor']
        book.idgenre=data['idgenre']
        db.session.commit()
        return jsonify({'message': 'Book updated'}), 200
    return jsonify({'message': 'Book not found'}), 404

@book_bp.route('/book/<isbn>', methods=['DELETE'])
def deleteBookById(isbn):
    book = Book.query.get(isbn)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted'}), 200
    return jsonify({'message': 'Book not found'}), 404

@book_bp.route('/book/<isbn>/order', methods=['GET'])
def getOrdersByBook(isbn):
    if not Book.query.get(isbn):
        return jsonify({'message': 'Book not found'}), 404
    results = db.session.query(Book, Bookorder).join(Bookorder, Book.isbn == Bookorder.idbook).filter(Book.isbn == isbn).all()
    if not results:
        return jsonify({'message': 'No orders found for this book'}), 404
    order_list = []
    print(len(results))
    for book, order in results:
        if book.isbn == isbn:
            book_order_data = {
                'book_isbn': book.isbn,
                'book_title': book.title,
                'order_id': order.idorder,
                'order_quantity': order.quantity,
                'order_date': order.date,
                'order_is_entry': order.isentry,
                'order_note': order.note
            }
        order_list.append(book_order_data)
    return jsonify(order_list), 200

@book_bp.route('/book/<isbn>/order', methods=['POST'])
def createOrderByBook(isbn):
    if not Book.query.get(isbn):
        return jsonify({'message': 'Book not found'}), 404
    data = request.get_json()
    if data['quantity'] < 0:
        return jsonify({'message': 'Quantity cannot be a negative number'}), 400
    new_order = Bookorder(
        quantity=data['quantity'],
        date=data['date'],
        isentry=data['isentry'],
        note=data['note'],
        idbook=isbn
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'New book order created'}), 201
