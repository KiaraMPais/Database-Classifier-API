# Se realiza la clasificación de las columnas con expresiones regulares
import re
from app.core.db import DatabaseConnector

# Diccionario de las columnas con datos sensibles:
regex_patterns = {
    "EMAIL_ADDRESS": r".*email.*",
    "CREDIT_CARD_NUMBER": r".*credit.*card.*",
    "USERNAME": r".*user.*name.*",
}

def classify_database(db_id):
    # Conexión a la base de datos
    connection = DatabaseConnector.connect(db_info)
    cursor = connection.cursor()

    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    classification_result = {}

    for table in tables:
        cursor.execute(f"SHOW COLUMNS FROM {table[0]}")
        columns = cursor.fetchall()

        classification_result[table[0]] = []
        for column in columns:
            column_name = column[0]
            classified_type = "N/A"

            for data_type, pattern in regex_patterns.items():
                if re.match(pattern, column_name.lower()):
                    classification_result = data_type
                    break
            
            classification_result[table[0]].append({
                "column": column_name,
                "information_type": classified_type
            })

    cursor.close()
    connection.close()
    return classification_result