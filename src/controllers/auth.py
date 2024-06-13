from flask import jsonify, request
from src.models.UserModel import User

def register_user():
    data = request.get_json()
    user = User.from_dict(data)
    exist_user = User.get_by_username(user.user_id)
    if exist_user:
        return jsonify({'message': 'User already exists'}), 400
    User.Create(user)
    return jsonify({'message': 'User create succesfully'}), 201

def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.get_by_username(username)
    if user and User.check_password(user.password, password):
        return jsonify({'message': 'Login successful', 'user': User.to_dict(user)}), 200
    return jsonify({'message': 'Invalid username or password'}), 401