import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "API")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///meu_banco.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
