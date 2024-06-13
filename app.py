
from config import config
from flask_cors import CORS
from src import init_app

configuration = config['development']
app = init_app(configuration)

CORS(app)

if __name__ == '__main__':
    app.run()