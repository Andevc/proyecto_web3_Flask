from flask import Blueprint
from src.controllers.product import *

product_bp = Blueprint('product_bp', __name__)

product_bp.route('/', methods=['GET'])(get_all_products)
product_bp.route('/<product_id>', methods=['GET'])(get_product)

 