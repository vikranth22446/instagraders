# coding=utf-8
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Initial Configurations for the Flask App
    """
    CSRF_ENABLED = True
    DEBUG = False
    TESTING = False
    db_path = os.path.join(os.path.dirname(__file__), 'app.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(db_path)

    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    """
    Developmental Configurations
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Production Configurations
    """


pass


class TestingConfig(Config):
    """
    Testing Configurations
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
