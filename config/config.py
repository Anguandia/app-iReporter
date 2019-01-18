class Config:
    DEBUG = False
    CSRF_ENABLED = True


class Development(Config):
    DEBUG = True
    red_flags = {}


class Testing(Config):
    TESTING = True
<<<<<<< HEAD
    red_flags = {}
=======
    DEBUG = True
>>>>>>> parent of 73a4201... rearrange config file


class Production(Config):
    DEBUG = False
    TESTING = False


app_config = {
    'DEVELOPMENT': Development, 'TESTING': Testing, 'PRODUCTION': Production
    }
