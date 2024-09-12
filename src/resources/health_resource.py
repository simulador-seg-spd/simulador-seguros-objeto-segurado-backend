from flask import request
from flask_restful import Resource
from src.utils.response_utils import resp_ok

RESOURCE_NAME = "HealthResource"
class HealthResource(Resource):
  def __init__(self):
    self.session_id = request.headers.get("sessionId")
    self.transaction_id = request.headers.get("transaction_id")

  def get(self):
    return resp_ok(resource=RESOURCE_NAME)