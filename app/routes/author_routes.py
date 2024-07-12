from flask import Blueprint, jsonify, request
from app.models import db, Author

author_bp = Blueprint('author_bp', __name__)

# -------------- ROUTES --------------

@author_bp.route('/author', methods=['GET'])
def getAuthors():
    authors = Author.query.all()
    authors_list = []
    for author in authors:
        author_data = {
            'idauthor': author.idauthor,
            'firstname': author.firstname,
            'lastname': author.lastname,
            'biography': author.biography
        }
        authors_list.append(author_data)
    return jsonify(authors_list), 200

@author_bp.route('/author/<int:id>', methods=['GET'])
def getAuthorById(id):
    author = Author.query.get(id)
    if author:
        author_data = {
            'idauthor': author.idauthor,
            'firstname': author.firstname,
            'lastname': author.lastname,
            'biography': author.biography
        }
        return jsonify(author_data), 200
    return jsonify({'message': 'Author not found'}), 404

@author_bp.route('/author', methods=['POST'])
def createAuthor():
    data = request.get_json()
    new_author = Author(firstname=data['firstname'], lastname=data['lastname'], biography=data['biography'])
    db.session.add(new_author)
    db.session.commit()
    return jsonify({'message': 'New author created'}), 201

@author_bp.route('/author/<int:id>', methods=['PUT'])
def updateAuthorById(id):
    data = request.get_json()
    author = Author.query.get(id)
    if author:
        author.firstname = data['firstname']
        author.lastname = data['lastname']
        author.biography = data['biography']
        db.session.commit()
        return jsonify({'message': 'Author updated'}), 200
    return jsonify({'message': 'Author not found'}), 404

@author_bp.route('/author/<int:id>', methods=['DELETE'])
def deleteAuthorById(id):
    author = Author.query.get(id)
    if author:
        db.session.delete(author)
        db.session.commit()
        return jsonify({'message': 'Author deleted'}), 200
    return jsonify({'message': 'Author not found'}), 404
