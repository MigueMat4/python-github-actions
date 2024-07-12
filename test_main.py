import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def new_author():
    return {'firstname': 'Stephen', 'lastname': 'King', 'biography': 'Escritor estadounidense de novelas de terror, ficción sobrenatural.'}

@pytest.fixture
def new_genre():
    return {'name': 'Non Fiction', 'description': 'Es un contenido, cuyo creador, en buena fe, asume la responsabilidad de la veracidad o exactitud de los eventos, personas o información presentada-'}

@pytest.fixture
def new_book():
    return {'isbn': '1234567890112', 'title': 'Las crónicas de Narnia', 'idauthor': 1, 'idgenre': 1,
            'price': 40, 'quantity': 1, 'language': 'Español', 'editorial': 'CBN books', 'pages': 120}

def test_get_main(client):
    response = client.get('/')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['message'] == 'Hello, welcome to Book Inventory Management System API'

def test_get_authors(client):
    response = client.get('/author')
    assert response.status_code == 200

def test_create_author(client, new_author):
    response = client.post('/author', json=new_author)
    json_data = response.get_json()
    assert response.status_code == 201
    assert json_data['message'] == 'New author created'

def test_get_author_by_id(client, new_author):
    response = client.get('/author/4')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['firstname'] == new_author['firstname']
    assert json_data['lastname'] == new_author['lastname']
    assert json_data['biography'] == new_author['biography']

def test_get_genres(client):
    response = client.get('/genre')
    json_data = response.get_json()
    assert response.status_code == 200

def test_create_genre(client, new_genre):
    response = client.post('/genre', json=new_genre)
    json_data = response.get_json()
    assert response.status_code == 201
    assert json_data['message'] == 'New genre created'

def test_get_genre_by_id(client, new_genre):
    response = client.get('/genre/2')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['name'] == new_genre['name']
    assert json_data['description'] == new_genre['description']

def test_get_books(client):
    response = client.get('/book')
    assert response.status_code == 200

def test_create_book(client, new_book):
    response = client.post('/book', json=new_book)
    json_data = response.get_json()
    assert response.status_code == 201
    assert json_data['message'] == 'New book created'

def test_get_book_by_id(client, new_book):
    response = client.get('/book/1234567890112')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['isbn'] == new_book['isbn']
    assert json_data['title'] == new_book['title']
    assert json_data['price'] == new_book['price']
    assert json_data['quantity'] == new_book['quantity']
    assert json_data['language'] == new_book['language']
    assert json_data['editorial'] == new_book['editorial']
    assert json_data['pages'] == new_book['pages']
    assert json_data['author']['idauthor'] == new_book['idauthor']
    assert json_data['genre']['idgenre'] == new_book['idgenre']
