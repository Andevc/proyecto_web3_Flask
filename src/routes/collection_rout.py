from flask import Blueprint
from src.controllers.collection_controller import *

collection_bp = Blueprint('collection_bp', __name__)

collection_bp.route('/user/<int:user_id>/collection', methods=['GET'])(get_products_by_user_id)
