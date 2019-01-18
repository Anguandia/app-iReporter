class Config:
    DEBUG = False
    CSRF_ENABLED = True


class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True
    DEBUG = True


class Production(Config):
    DEBUG = False
    TESTING = False


app_config = {
    'DEVELOPMENT': Development, 'TESTING': Testing, 'PRODUCTION': Production
    }
