from flask import Blueprint
from src.controllers.user import *
from src.controllers.collection_controller import get_products_by_user_id
from src.controllers.product import create_product_for_user
user_bp = Blueprint('user_bp', __name__)


user_bp.route('/', methods=['GET'])(get_all_users)
user_bp.route('/<int:user_id>', methods=['GET'])(get_user)
user_bp.route('/edit/<int:user_id>', methods=['PUT'])(update_user)
user_bp.route('/delete/<int:user_id>', methods=['DELETE'])(delete_user)
user_bp.route('/<int:user_id>/collection', methods=['GET'])(get_products_by_user_id)
