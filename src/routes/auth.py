from flask import Blueprint
from src.controllers.auth_controller import *

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/register', methods=['POST'])(register_user)
auth_bp.route('/login', methods=['POST'])(login_user)