import os
import uuid
import logging

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from src.infra.logs.custom_json_formatter import CustomJsonFormatter
from src.routes import config_resource_routes


APP_NAME = "simulador-seguros-objeto-segurado-backend"

file_dir = os.path.split(os.path.realpath(__file__))[0]
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logHandler = logging.StreamHandler()
formatter = CustomJsonFormatter("%(timestamp)s %(levelname)s %(message)s", json_ensure_ascii=False)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

loggerFile = logging.FileHandler(f"{file_dir}/{APP_NAME}.log")
loggerFile.setFormatter(formatter)
logger.addHandler(loggerFile)


def config_routes(app):
  BASE_PATH_HTTP = "/"
  api = Api()
  api.prefix = BASE_PATH_HTTP
  config_resource_routes(api)
  app.config["resource_list"] = api.resources
  api.init_app(app)

def set_swagger(app):
    """
      Adiciona uma rota de `swagger`
    """
    swagger_url = "/docs"
    swaggerui_blueprint = get_swaggerui_blueprint(swagger_url, "/api-docs", config={"app_name": APP_NAME})
    app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)


class InterceptRequestMiddleware:
  def __init__(self, wsgi_app):
    self.wsgi_app = wsgi_app
  def __call__(self, environ, start_response):
    if not environ.get("HTTP_TRANSACTION_ID"):
      environ["HTTP_TRANSACTION_ID"] = uuid.uuid4().hex
    return self.wsgi_app(environ, start_response)

def app_start():
  CONFIG = "Config"
  app = Flask(__name__)
  app.wsgi_app = InterceptRequestMiddleware(app.wsgi_app)
  app.config.from_object(f"settings.{CONFIG}")
  config_routes(app)
  set_swagger(app)
  os.environ["APP_NAME"] = APP_NAME
  CORS(app, resources={r"*": {"origins": "*"}})
  return app

app = app_start()
if __name__ == "__main__":
  app.run(debug=False, host="0.0.0.0", port=8080)