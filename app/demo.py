import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"), 
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    port = os.getenv("DB_PORT"),
    sslmode='require',
)
cur = conn.cursor()
cur.execute(f"INSERT INTO items (name, price) VALUES ('Honda', '20000') RETURNING id")
item_id = cur.fetchone()[0]
conn.commit()
print(item_id)


