from flask import jsonify, request
from src.models.ProductModel import Product
from src.models.UserModel import User
from src.models.CollectionModel import Collection

def get_all_products():
    products = [Product.to_dict(prod) for prod in Product.get_All()]
    return jsonify(products), 200

def get_product(product_id):
    product = Product.to_dict(Product.get_by_Id(product_id))
    if product:
        return jsonify(product), 200
    
    return jsonify({'message': 'Producto not fund'}), 404


def create_product_for_user(user_id):
    try:
        data = request.get_json()

        new_product = Product.from_dict(data)
        Product.Create(new_product)
        
        created_product = Product.get_by_Id(new_product.product_id)

        add_product_to_collection = Collection(user_id, created_product.product_id)
        Collection.add_product_to_user_collection(add_product_to_collection)

        return jsonify({'message' : 'Product created successfully', 'product': Product.to_dict(created_product)}), 500
    except Exception as e:
        return jsonify({'message': str(e)}), 500

    