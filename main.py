from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    phone = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'Имя: {self.name}. Номер: {self.phone}'

@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    data = request.get_json()
    if not data or 'name' not in data or 'phone' not in data:
        return jsonify({'error': 'Неверные данные'}), 400

    contact = Contact(name=data['name'], phone=data['phone'])
    db.session.add(contact)
    db.session.commit()

    return jsonify({
        'message': 'Контакт успешно добавлен',
        'contact': {'id': contact.id, 'name': contact.name, 'phone': contact.phone}
    }), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
