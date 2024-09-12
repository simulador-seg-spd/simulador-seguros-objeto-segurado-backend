from datetime import datetime

import click
from flask import request
from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
  def add_fields(self, log_record, record, message_dict, ensure_ascii=False):
    if isinstance(record.msg, str):
      record.msg = click.unstyle(record.msg)
    if isinstance(record.message, str):
      record.message = click.unstyle(record.message)
    super().add_fields(log_record, record, message_dict)

    log_record["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    if request:
      log_record["session_id"] = request.headers.get("session_id")
      log_record["transaction_id"] = request.headers.get("transaction_id")
      try:
        req = request.get_json(force=True) or {}
      except Exception:
        req = {}
      log_record["profileName"] = req.get("profileName")
      log_record["path"] = request.path
      log_record["method"] = request.method