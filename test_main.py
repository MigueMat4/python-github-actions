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
