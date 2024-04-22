from flask import Flask, jsonify, request

books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]

app = Flask(__name__)

@app.route('/')
def home():
    return 'Nasa kniznica'

@app.route('/books/list', methods=['GET'])  # zoznam knih
def get_books():
    return jsonify({'books': books})

@app.route('/books/add', methods=['POST']) # pridat knihu
def add_book():
    print(request)
    new_book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:id>')  # zadanie 1  Ziskanie knizky podla ID
def ziskaj_book(id):
    for book in books:
        if book['id'] == id:
            return jsonify(book), 200
    return jsonify({'error': 'Kniha s daným ID neexistuje'}), 404

@app.route('/books/update/<int:id>', methods=['PUT'])    # zadanie 2  • Aktualizácia Knižky
def aktualizuj_knihu(id):
    data = request.get_json()
   # global books
    for book in books:
        if book['id'] == id:
            if 'title' in data:
                book['title'] = data['title']
            if 'author' in data:
                book['author'] = data['author']
            return jsonify(book), 200

    return jsonify({'error': 'Kniha s daným ID neexistuje'}), 404






@app.route('/books/delete/<int:id>', methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book['id'] == id:
            books.remove(book)
            return jsonify({'#>': 'Kniha bola úspešne odstránená'}), 200

    # Ak kniha s daným ID neexistuje, vráťte chybovú správu 404 Not Found
    return jsonify({'error': 'Kniha s daným ID neexistuje'}), 404






if __name__ == "__main__":
    app.run()