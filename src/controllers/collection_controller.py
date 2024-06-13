from src.models.CollectionModel import Collection
from src.models.ProductModel import Product
from src.models.UserModel import User

from flask import jsonify

def get_products_by_user_id(user_id):
    try:
        user = User.to_dict(User.get_by_Id(user_id))
        if not user:
            return jsonify({'message': 'User nor found'}), 404
        
        products = Collection.get_products_by_user_id(user_id)
        product_list = [Product.to_dict(product) for product in products]

        user['products'] = product_list

        return jsonify(user), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 500


