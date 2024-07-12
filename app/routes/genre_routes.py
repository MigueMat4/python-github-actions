from flask import Blueprint, jsonify, request
from app.models import db, Genre

genre_bp = Blueprint('genre_bp', __name__)

# -------------- ROUTES --------------

@genre_bp.route('/genre', methods=['GET'])
def getGenres():
    genres = Genre.query.all()
    genres_list = []
    for genre in genres:
        genre_data = {
            'idgenre': genre.idgenre,
            'name': genre.name,
            'description': genre.description
        }
        genres_list.append(genre_data)
    return jsonify(genres_list), 200

@genre_bp.route('/genre/<int:id>', methods=['GET'])
def getGenreById(id):
    genre = Genre.query.get(id)
    if genre:
        genre_data = {
            'idgenre': genre.idgenre,
            'name': genre.name,
            'description': genre.description
        }
        return jsonify(genre_data), 200
    return jsonify({'message': 'Genre not found'}), 404

@genre_bp.route('/genre', methods=['POST'])
def createGenre():
    data = request.get_json()
    new_genre = Genre(name=data['name'], description=data['description'])
    db.session.add(new_genre)
    db.session.commit()
    return jsonify({'message': 'New genre created'}), 201

@genre_bp.route('/genre/<int:id>', methods=['PUT'])
def updateGenreById(id):
    data = request.get_json()
    genre = Genre.query.get(id)
    if genre:
        genre.name = data['name']
        genre.description = data['description']
        db.session.commit()
        return jsonify({'message': 'Genre updated'}), 200
    return jsonify({'message': 'Genre not found'}), 404

@genre_bp.route('/genre/<int:id>', methods=['DELETE'])
def deleteGenreById(id):
    genre = Genre.query.get(id)
    if genre:
        db.session.delete(genre)
        db.session.commit()
        return jsonify({'message': 'Genre deleted'}), 200
    return jsonify({'message': 'Genre not found'}), 404
