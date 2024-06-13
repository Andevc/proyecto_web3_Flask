from flask import jsonify, request
from src.database.db_mysql import DataBase

from src.models.ProductModel import Product
from src.models.CollectionModel import Collection

from src.services.cloudinary_service import get_url_from_cloudinary
from src.utils.generate_id import generate_id

def get_all_products():
    products = [Product.to_dict(prod) for prod in Product.get_All()]
    return jsonify(products), 200

def get_product(product_id):
    product = Product.to_dict(Product.get_by_Id(product_id))
    if product:
        return jsonify(product), 200
    
    return jsonify({'message': 'Producto not fund'}), 404


def create_product_for_user(user_id):
    db = DataBase()
    try:

        #data = request.form
        # image_file = data.files['image']
        # image_name = data.files['image_tittle']
        # url_image = get_url_from_cloudinary(image_file, image_name)

        # if not url_image:
        #     return jsonify({'message' : 'Error to upload file'}), 500

        # new_product = Product( 
        #     product_id=generate_id(), 
        #     product_name=data['name'], 
        #     description=data['description'], 
        #     price=data['price'], 
        #     image_url=url_image
        # )
        
        #-------------------------------------------------
        data = request.get_json()

        if data['product_id'] == "":
            data['product_id'] = generate_id()
            print(data['product_id'])
        #-------------------------------------------------

        new_product = Product.from_dict(data)

        exist_product = Product.get_by_Id(new_product.product_id)

        if exist_product:
            return jsonify({'message' : 'Product already exist.'}), 400
        
        db.conecction.begin()
        Product.Create(new_product)
        print(user_id, new_product.product_id)

        Collection.add_product_to_user_collection(user_id, new_product.product_id)
        db.conecction.commit()

        return jsonify({'message' : 'Product created successfully', 'product': Product.to_dict(new_product)}), 200
    
    except Exception as e:

        db.conecction.rollback()
        return jsonify({'message': str(e)}), 500
    
    finally:

        db.close()


        if data['product_id'] == "":
            data['product_id'] = generate_id()
            print(data['product_id'])

        new_product = Product.from_dict(data)


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