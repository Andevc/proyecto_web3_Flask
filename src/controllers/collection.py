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
        products_list = [Product.to_dict(product) for product in products]
        
        count_products = Collection.count_products_from_user(user_id)

        user['quantity_products'] = count_products
        user['products'] = products_list

        return jsonify(user), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
    
def delete_acount_and_products(user_id):
    try:
        user = User.to_dict(User.get_by_Id(user_id))
        if not user:
            return jsonify({'message': 'User nor found'}), 404
        
        products = Collection.get_products_by_user_id(user_id)
    
        all_products = [Product.from_dict(Product.to_dict(product)) for product in products]
        for prod in all_products:
            print(str(prod))
            collection = Collection.get_by_user_and_product_id(user_id, prod.product_id)
            if collection:
                Collection.delete_from_collection(user_id, prod.product_id)
                Product.Delete(prod.product_id)

        User.Delete(user_id)

        return jsonify({'message' : 'Delete acount succesfully and all products removed from collection.'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
