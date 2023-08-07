import logging

from flask import Flask
from flask_migrate import Migrate, MigrateCommand


from flask.cli import FlaskGroup
from flask_sqlalchemy import SQLAlchemy

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = FlaskGroup(app)
manager.add_command('db', MigrateCommand)

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)  # Устанавливаем уровень логирования

# Создаем объект логгера для SQLAlchemy
logger = logging.getLogger('sqlalchemy.engine')
handler = logging.FileHandler('sqlalchemy.log')  # Задаем файл для записи логов
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
