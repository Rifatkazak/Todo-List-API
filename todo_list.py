from flask import Blueprint, request, jsonify
from models import db, Todo, User
from functools import wraps
import jwt

todo_list_bp = Blueprint('todo_list', __name__)

# Token doğrulama fonksiyonu
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            decoded_token = jwt.decode(token, 'secret_key', algorithms=['HS256'])
            current_user = User.query.filter_by(id=decoded_token['user_id']).first()
        except Exception as e:
            return jsonify({'message': 'Invalid token!'}), 403

        return f(current_user, *args, **kwargs)
    return decorated_function


# To-Do listesi oluşturma
@todo_list_bp.route('/todos', methods=['POST'])
@token_required
def create_todo(current_user):
    data = request.get_json()
    title = data.get('title')

    if not title:
        return jsonify({"message": "Title is required!"}), 400

    new_todo = Todo(title=title, user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({"message": "Todo created successfully!"}), 201


# Tüm To-Do'ları listeleme
@todo_list_bp.route('/todos', methods=['GET'])
@token_required
def get_all_todos(current_user):
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    todo_list = [{"id": todo.id, "title": todo.title, "completed": todo.completed} for todo in todos]

    return jsonify(todo_list), 200


# To-Do güncelleme
@todo_list_bp.route('/todos/<int:todo_id>', methods=['PUT'])
@token_required
def update_todo(current_user, todo_id):
    data = request.get_json()
    title = data.get('title')

    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()
    if not todo:
        return jsonify({"message": "Todo not found!"}), 404

    todo.title = title if title else todo.title
    todo.completed = data.get('completed', todo.completed)

    db.session.commit()

    return jsonify({"message": "Todo updated successfully!"}), 200


# To-Do silme
@todo_list_bp.route('/todos/<int:todo_id>', methods=['DELETE'])
@token_required
def delete_todo(current_user, todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()
    if not todo:
        return jsonify({"message": "Todo not found!"}), 404

    db.session.delete(todo)
    db.session.commit()

    return jsonify({"message": "Todo deleted successfully!"}), 200
