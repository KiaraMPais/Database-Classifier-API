# Permitir la conexion a diferentes tipos de bases de datos relacionales (modular)
import mysql.connector
from app.core.config import settings
# Se pueden agregar las librerias para conectar con la base de datos que se desea.

class DatabaseConnector:

    @staticmethod
    def connect(db_info):
        if db_info.dbname == "mysql":
            return DatabaseConnector._connect_mysql(db_info)
        # Si se necesita se pueden agregar más IF con otras posibles conexiones a otros tipos de bases de datos.
        else:
            raise ValueError(f"Database type '{db_info.dbname}' not supported")
        
    @staticmethod
    def _connect_mysql(db_info):
        try:
            conn = mysql.connector.connect(
                host=settings.DB_HOST,
                port=settings.DB_PORT,
                user=settings.DB_USER,
                password=settings.DB_PASSWORD,
                database=settings.DB_NAME
            )
            return conn
        except mysql.connector.Error as err:
            raise ConnectionError(f"Error connecting to MySQL: {err}")