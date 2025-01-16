import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secure_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///transactions.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
