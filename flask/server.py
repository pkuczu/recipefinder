from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ingredients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(255), nullable=False)

if not os.path.exists('ingredients.db'):
    with app.app_context():
        db.create_all()

@app.route('/addIngredients', methods=['POST'])
def add_ingredients():
    try:
        data = request.get_json()

        if 'ingredients' not in data:
            return jsonify({'error': 'Invalid request. Missing "ingredients" key.'}), 400

        ingredients = data['ingredients']

        for ingredient in ingredients:
            new_ingredient = Ingredient(service=ingredient['service'])
            db.session.add(new_ingredient)

        db.session.commit()

        return jsonify({'message': 'Ingredients added successfully!'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5173)


# TESTING
import requests
import json

url = 'http://127.0.0.1:5173/addIngredients'
headers = {'Content-Type': 'application/json'}
data = {'ingredients': [{'service': 'ingredient1'}, {'service': 'ingredient2'}]}

response = requests.post(url, headers=headers, data=json.dumps(data))
