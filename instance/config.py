class Config():
    DEBUG=False

class DevelopmentConfig(Config):
    """
    Enable our debug mode to True
    in development in order to auto
    restart our server on code changes
    """
    DEBUG = True

app_configuration={
    'development': DevelopmentConfig
}

AppConfig = app_configuration.get('development')

