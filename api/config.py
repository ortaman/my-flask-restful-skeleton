
import os


class Config(object):
    DEBUG = False


class DevelopmentConfig(Config):
    CRYPTO_KEY = b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg='
    DEBUG = True
    ENV = 'development'
    HOST = '0.0.0.0'
    PORT = '5050'

class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}

config_name = os.getenv('FLASK_ENV', 'development')
env_class = app_config[config_name]

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CRYPTO_KEY = env_class.CRYPTO_KEY

HOST = env_class.HOST
PORT = env_class.PORT
