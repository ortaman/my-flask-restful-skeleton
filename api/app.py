
import os
from flask import Flask, Blueprint
from flask_restful import Api

from resources.index import IndexResource
from resources.todo import TodotResource, TodotResourceList
from config import app_config, HOST, PORT


def create_app(config_env):
    app = Flask(__name__)
    app.config.from_object(app_config[config_env])

    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)

    # Routes
    api.add_resource(IndexResource, '/')
    api.add_resource(TodotResourceList, '/todos')
    api.add_resource(TodotResource, '/todos/<string:todo_id>')

    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app


if __name__ == "__main__":
    config_env = os.getenv('FLASK_ENV', 'development')

    app = create_app(config_env)
    app.run(host=HOST, port=PORT)
