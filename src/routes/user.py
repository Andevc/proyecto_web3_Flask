from flask import Blueprint
from src.controllers.user import *
from src.controllers.collection import *
from src.controllers.product import *

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(get_all_users)
user_bp.route('/<int:user_id>/', methods=['GET'])(get_user)
user_bp.route('/edit-profile/<int:user_id>/', methods=['PUT'])(update_user)
user_bp.route('/delete-acount/<int:user_id>/', methods=['DELETE'])(delete_acount_and_products)

user_bp.route('/<int:user_id>/collection/', methods=['GET'])(get_products_by_user_id)

user_bp.route('/<int:user_id>/collection/create-product/', methods=['POST'])(create_product_for_user)
user_bp.route('/<int:user_id>/collection/edit-product/<int:product_id>/', methods=['PUT'])(update_product)
user_bp.route('/<int:user_id>/collection/deleteProduct/<int:product_id>/', methods=['DELETE'])(delete_product)
