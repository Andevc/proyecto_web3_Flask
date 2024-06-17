from flask import Blueprint
from src.controllers.user import *
from src.controllers.collection import *
from src.controllers.product import *

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(get_all_users)
user_bp.route('/<user_id>', methods=['GET'])(get_user)
user_bp.route('/edit-profile/<user_id>', methods=['PUT'])(update_user)
user_bp.route('/delete-acount/<user_id>', methods=['DELETE'])(delete_acount_and_products)#del controlador collection

user_bp.route('/collection/<user_id>', methods=['GET'])(get_products_by_user_id)#del controlador collection

user_bp.route('/collection/<user_id>/create-product', methods=['POST'])(create_product_for_user) # controlador product
user_bp.route('/collection/<user_id>/edit-product/<product_id>', methods=['PUT'])(update_product) # controlador product
user_bp.route('/collection/<user_id>/deleteProduct/<product_id>', methods=['DELETE'])(delete_product) # controlador product
