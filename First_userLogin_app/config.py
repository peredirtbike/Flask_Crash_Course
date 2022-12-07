class Config:
    SECRET_KEY = 'secretKey'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:''@localhost:3306/myflask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_TIMEOUT= 10