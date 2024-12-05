import os


class Config:
    
    SECRET_KEY = 'cc1954a0b2fa7878e90d95eb1bfbcae8'
    SQLALCHEMY_DATABASE_URI ='sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS_MAIL')