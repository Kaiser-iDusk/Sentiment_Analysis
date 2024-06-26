import os
import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

external_var = "postgresql://users_db_n95m_user:k1utNV6zjMigFYGYoIWlifWinDZ66G3K@dpg-cprcsljv2p9s73a4kl8g-a.oregon-postgres.render.com/users_db_n95m"
internal_var = "postgresql://users_db_n95m_user:k1utNV6zjMigFYGYoIWlifWinDZ66G3K@dpg-cprcsljv2p9s73a4kl8g-a/users_db_n95m"
app = Flask(__name__)

app.config['SECRET_KEY'] = "super_secret_key"
os.environ["DATABASE_URL"] = internal_var
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
# postgresql://users_db_n95m_user:k1utNV6zjMigFYGYoIWlifWinDZ66G3K@dpg-cprcsljv2p9s73a4kl8g-a.oregon-postgres.render.com/users_db_n95m
db = SQLAlchemy(app)

from app_files import routes