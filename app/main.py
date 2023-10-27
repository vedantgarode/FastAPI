from fastapi import Depends, FastAPI, HTTPException, Header
from fastapi.responses import FileResponse
from pydantic import BaseModel
import psycopg2
from secrets import token_urlsafe
import os
from dotenv import load_dotenv

load_dotenv()

# Define the data models using Pydantic
class Item(BaseModel):
    name: str
    price: int

class APIKey(BaseModel):
    key: str
    username: str

# Function to validate the API key
def validate_api_key(api_key: str):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT api_key FROM users WHERE api_key = '{api_key}'")
    valid_key = cur.fetchone()
    conn.close()
    return valid_key is not None

# Function to get the API key from the request headers
async def get_api_key(api_key: str = Header(None)):
    if not api_key or not validate_api_key(api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key

# Function to establish a database connection
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"), 
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        port = os.getenv("DB_PORT"),
        sslmode='require',
    )
    return conn

# Function to create the 'items' table if it doesn't exist
def create_items_table_if_not_exist():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                price NUMERIC(10, 2) NOT NULL
            );
        """)
        conn.commit()

        conn.close()
    except Exception as e:
        print(f"Error creating 'items' table: {e}")

# Function to create the 'users' table if it doesn't exist
def create_users_table_if_not_exist():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                api_key VARCHAR(255) NOT NULL
            );
        """)
        conn.commit()

        conn.close()
    except Exception as e:
        print(f"Error creating 'users' table: {e}")

# Create a FastAPI instance
app = FastAPI()

# Event handler to create tables when the application starts

    

# Serve the index.html page from the 'static' directory
@app.get("/")
async def read_index():
    create_items_table_if_not_exist()
    create_users_table_if_not_exist()
    return FileResponse('static/index.html')

# Generate a new API key for a user
@app.get("/generate_key/")
def key_generator(user_name: str):
    create_items_table_if_not_exist()
    create_users_table_if_not_exist()
    conn = get_db_connection()
    cur = conn.cursor()

    # Check if the username already exists
    cur.execute("SELECT username FROM users WHERE username = %s", (user_name,))
    existing_username = cur.fetchone()

    if existing_username:
        conn.close()
        raise HTTPException(status_code=400, detail="Username already exists")

    # Generate a new API key
    new_api_key = token_urlsafe(16)

    # Insert the new user
    cur.execute("INSERT INTO users (username, api_key) VALUES (%s, %s)", (user_name, new_api_key))
    conn.commit()

    conn.close()
    return {"status": "User Added", "APIKey": APIKey(key=new_api_key, username=user_name)}

# Create a new item in the 'items' table
@app.post("/add_item/")
def create_item(item: Item, api_key: str = Depends(get_api_key)):
    create_items_table_if_not_exist()
    create_users_table_if_not_exist()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO items (name, price) VALUES ('{item.name}', '{item.price}') RETURNING id")
    item_id = cur.fetchone()[0]
    conn.commit()
    return {"status": "Item created", "id": item_id}

# Retrieve all items from the 'items' table
@app.get("/get_items/")
async def read_items(api_key: str = Depends(get_api_key)):
    create_items_table_if_not_exist()
    create_users_table_if_not_exist()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM items")
    items = cur.fetchall()
    col_names = [desc[0] for desc in cur.description]

    item_list = []
    for item in items:
        item_dict = {}
        for i in range(len(col_names)):
            item_dict[col_names[i]] = item[i]
        item_list.append(item_dict)

    conn.close()

    return {"items": item_list}

# Retrieve a specific item by ID from the 'items' table
@app.get("/get_item/{item_id}")
async def read_item(item_id: int, api_key: str = Depends(get_api_key)):
    create_items_table_if_not_exist()
    create_users_table_if_not_exist()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM items WHERE id = {item_id}")
    items = cur.fetchall()
    col_names = [desc[0] for desc in cur.description]

    item_list = []
    for item in items:
        item_dict = {}
        for i in range(len(col_names)):
            item_dict[col_names[i]] = item[i]
        item_list.append(item_dict)

    conn.close()

    return {"item": item_list}

# Update a specific item by ID in the 'items' table
@app.put("/item/{item :Item}")
async def update_item( item :Item,  api_key: str = Depends(get_api_key)):
    create_items_table_if_not_exist()
    create_users_table_if_not_exist()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE items SET name = %s, price = %s WHERE id = %s", (item.name, item.price, item.id))
    conn.commit()
    return {"status": "Item updated"}

# Delete a specific item by ID from the 'items' table
@app.delete("/items/{item_id}")
async def delete_item(item_id: int, api_key: str = Depends(get_api_key)):
    create_items_table_if_not_exist()
    create_users_table_if_not_exist()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM items WHERE id = %s", (item_id,))
    conn.commit()
    return {"status": "Item deleted"}