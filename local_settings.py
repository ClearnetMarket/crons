# coding=utf-8

#SQLALCHEMY_DATABASE_URI_0 = database_connection
class ConfigMain:

    # databases info
    POSTGRES_USERNAME = 'postgres'
    POSTGRES_PW = 'password'
    POSTGRES_SERVER = 'database:5432'
    POSTGRES_DBNAME00 = 'clearnet'
    SQLALCHEMY_DATABASE_URI_0 = "postgresql+psycopg2://{}:{}@{}/{}".format(POSTGRES_USERNAME,
                                                                           POSTGRES_PW,
                                                                           POSTGRES_SERVER,
                                                                           POSTGRES_DBNAME00)
    SQLALCHEMY_BINDS = {'clearnet': SQLALCHEMY_DATABASE_URI_0}

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_FILES_DEST = '/mnt/clearnet'
    UPLOADED_FILES_DEST_ITEM = '/mnt/clearnet/item'
    UPLOADED_FILES_DEST_USER = '/mnt/clearnet/user'
 