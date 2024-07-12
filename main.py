# By: Miguel Matul Calderón

from flask import Flask, jsonify
from app.models import db
from app.routes.author_routes import author_bp
from app.routes.genre_routes import genre_bp
from app.routes.book_routes import book_bp

# -------------- SETUP --------------

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Test12345@localhost/laserants_bims'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# -------------- ROUTES --------------

app.register_blueprint(author_bp)
app.register_blueprint(genre_bp)
app.register_blueprint(book_bp)

@app.route('/', methods=['GET'])
def main():
    return jsonify({'message': 'Hello, welcome to Book Inventory Management System API'}), 200

# -------------- MAIN --------------

if __name__ == '__main__':
    app.run()
