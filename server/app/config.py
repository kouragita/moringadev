import os

class Config:
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///moringadaily.db'
    # SQLALCHEMY_DATABASE_URI = 'postgress-server under here'
    SQLALCHEMY_TRACK_MODIFICATIONS = False