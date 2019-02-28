class Config (object) :
    """
    COMMON CONFIGURATION
    """
    # Put common configurations shared across environments


class DevelopmentConfig (Config) :
    """
    DEVELOPMENT CONFIGURATION
    """
    # Enable Flask's debugging features.
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig (Config) :
    """
    PRODUCTION CONFIGURATIONS
    """

    DEBUG = False


app_config = {
    'development' : DevelopmentConfig,
    'Production'  : ProductionConfig
}
