from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)


 #Настройка логирования
logging.basicConfig(level=logging.DEBUG)  # Устанавливаем уровень логирования

# Создаем объект логгера для SQLAlchemy
logger = logging.getLogger('sqlalchemy.engine')
handler = logging.FileHandler('sqlalchemy.log')  # Задаем файл для записи логов
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)