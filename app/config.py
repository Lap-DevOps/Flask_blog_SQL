class Configuration(object):
    DEBUG = True
    SECRET_KEY = 'your_secret_key'

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:qwaszx12@localhost/test1?auth_plugin=mysql_native_password'

    SQLALCHEMY_TRACK_MODIFICATION = False

    SQLALCHEMY_ECHO = True

    SECURITY_PASSWORD_SALT = 'kjsdhkjsdkjhkjds'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
