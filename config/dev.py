import os


DEBUG = True
SECRET_KEY = os.environ.get('DB_SECRET_KEY')
SQLALCHEMY_DATABASE_URI= f"postgresql://postgres:{SECRET_KEY}@localhost:5432/bookstore"
SQLALCHEMY_TRACK_MODIFICATIONS=False

