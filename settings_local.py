

class ApplicationConfig:
    CURRENT_SETTINGS = 'LOCAL'
    # databases info
    POSTGRES_USERNAME = 'postgres'
    POSTGRES_PW = 'postgres'
    POSTGRES_SERVER = 'database:5432'
    POSTGRES_DBNAME00 = 'clearnet'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{}:{}@{}/{}".format(POSTGRES_USERNAME,
                                                                        POSTGRES_PW,
                                                                        POSTGRES_SERVER,
                                                                        POSTGRES_DBNAME00)
    SQLALCHEMY_BINDS = {'clearnet': SQLALCHEMY_DATABASE_URI}

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_FILES_DEST_ITEM = '/data/item'
    UPLOADED_FILES_DEST_USER = '/data/user'
    UPLOADED_FILES_ALLOW = ['png', 'jpeg', 'jpg', 'png', 'gif']
