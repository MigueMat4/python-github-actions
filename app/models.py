from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# -------------- MODELS --------------

class Author(db.Model):
    idauthor = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(255), nullable = False)
    lastname = db.Column(db.String(255), nullable = False)
    biography = db.Column(db.Text, nullable = True) # As MEDIUMTEXT in MySql

    def __repr__(self):
        return f'<Author: {self.firstname}, {self.lastname}>'
    
class Genre(db.Model):
    idgenre = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    description = db.Column(db.Text, nullable = True) # As TINYTEXT in MySql

    def __repr__(self):
        return f'<Genre: {self.name}>'
    
class Book(db.Model):
    isbn = db.Column(db.String(45), primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    price = db.Column(db.Float, nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    language = db.Column(db.String(255), nullable = False)
    editorial = db.Column(db.String(255), nullable = False)
    pages = db.Column(db.Integer, nullable = False)
    idauthor = db.Column(db.Integer, db.ForeignKey('author.idauthor'), nullable=False)
    author = db.relationship('Author', backref=db.backref('books', lazy=True))
    idgenre = db.Column(db.Integer, db.ForeignKey('genre.idgenre'), nullable=False)
    genre = db.relationship('Genre', backref=db.backref('books', lazy=True))

class Bookorder(db.Model):
    idorder = db.Column(db.Integer, primary_key = True)
    quantity = db.Column(db.Integer, nullable = False)
    date = db.Column(db.String(255), nullable = False)
    isentry = db.Column(db.Boolean, nullable=False)
    note = db.Column(db.String(255), nullable = False)
    idbook = db.Column(db.Integer, db.ForeignKey('book.isbn'), nullable=False)
    book = db.relationship('Book', backref=db.backref('bookorders', lazy=True))
