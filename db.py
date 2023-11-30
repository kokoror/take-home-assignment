import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')

db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    passwd=db_pass
)

cursorObject = db.cursor()

cursorObject.execute(f"CREATE DATABASE {db_name}")

print(f'Database {db_name} created!')