from dotenv import load_dotenv
import os

load_dotenv()

class Config :

    DATABASE_URL = os.getenv('DATABASE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')

class DevelopmentConfig(Config) :
    DEBUG = True

class ProductionsConfig(Config) :
    DEBUG = False

config = {
    'DevelopmentConfig' : DevelopmentConfig,
    'ProductionsConfig' : ProductionsConfig,
    'Default' : DevelopmentConfig
}