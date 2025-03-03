from flask import Flask
from flask_mail import Mail
from .config import Config
from flask_wtf.csrf import CSRFProtect

from flask_mail import Mail
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
SECRET_KEY = 'Sup3r$3cretkey'
csrf = CSRFProtect(app)
            
from app import views