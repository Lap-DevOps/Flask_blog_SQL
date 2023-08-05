from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Замените следующие значения на свои
DB_USER = 'root'
DB_PASSWORD = 'qwaszx12'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'test1'

# Формируем строку подключения
db_uri = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Попытка подключения к базе данных
try:
    engine = create_engine(db_uri)
    connection = engine.connect()
    print("Connected to the database!")

    # Получение информации о версии сервера
    result = connection.execute("SELECT VERSION()")
    server_version = result.scalar()
    print("Server version:", server_version)

except SQLAlchemyError as e:
    print("Error connecting to the database:", e)

finally:
    if 'connection' in locals():
        connection.close()
