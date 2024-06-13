from flask import jsonify, request
from src.models.ProductModel import Product
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
        exist_product = Product.get_by_Id(new_product.product_id)
        if exist_product:
            return jsonify({'message' : 'Product already exist.'}), 400
        
        Product.Create(new_product)
        print(user_id, new_product.product_id)
        Collection.add_product_to_user_collection(user_id, new_product.product_id)

        return jsonify({'message' : 'Product created successfully', 'product': Product.to_dict(new_product)}), 200
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500

def update_product(product_id):
    Product.Update(product_id)
    return jsonify({'message' : 'Product edit succesfully'}), 200

def delete_product(user_id,product_id):
    collection = Collection.get_by_user_and_product_id(user_id, product_id)
    if collection:
        Collection.delete_from_collection(user_id, product_id)
        Product.Delete(product_id)
        return jsonify({'message' : 'Product delete succesfully'}), 200
    
    return jsonify({'message' : 'Unauthorized or Product not found'}), 403