from datetime import timedelta
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SECRET_KEY = "C0dGtV{c5cZ?u?er6%Gn"
SQLALCHEMY_TRACK_MODIFICATIONS = False

REMEBER_COOCKIE_DURATION = timedelta(days=5)