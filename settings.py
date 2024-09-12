import os

os.environ["TZ"] = "America/Sao_Paulo"

class Config(object):
    DEBUG = True
    TESTING = True
    JSON_AS_ASCII = False