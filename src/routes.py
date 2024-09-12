from flask_restful import Api
from src.resources.health_resource import HealthResource
from src.resources.objeto_segurado_resource import ObjetoSeguradoResource
def config_resource_routes(api: Api):
  BASE_PATH_HTTP = "/objeto-segurado"
  api.add_resource(
    ObjetoSeguradoResource,
    f"{BASE_PATH_HTTP}",
    methods=["POST","PUT","GET"],
    endpoint="ObjetoSegurado"
  )
  
  api.add_resource(
    HealthResource,
    f"{BASE_PATH_HTTP}/health",
    methods=["GET"],
    endpoint="ObjetoSeguradoHealth"
  )