from flask import jsonify, request
from src.models.UserModel import User


def get_all_users():
    users = [User.to_dict(user) for user in User.get_All()]
    return jsonify(users), 200

def get_user(user_id):
    user = User.to_dict(User.get_by_Id(user_id))
    if user:
        return jsonify(user), 200
    return jsonify({'message' : 'User not fund'}), 404

def update_user(user_id):
    data = request.get_json()
    user = User.from_dict(data)
    user.user_id = user_id
    User.Update(user)
    return jsonify({'message': 'User Update Seccesfully'}), 200

def delete_user(user_id):
    User.Delete(user_id)
    return jsonify({'message' : 'User Delete Succesfully'}), 200


