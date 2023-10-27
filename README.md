# Vedant FastAPI Application
-----------

This is the README documentation for a FastAPI application that provides a simple API for managing Items and API keys for users. The application uses PostgreSQL as a database backend.

# Description
-----------

The application is built with FastAPI, a modern, fast web framework for building APIs with Python 3.6+ based on standard Python type hints. It features automatic interactive API documentation, easy to learn, and is highly scalable [github.com](https://github.com/vedantgarode/FastAPI).

This application has various functionalities including user authentication using API keys, CRUD operations for items, and automatic creation of database tables at startup.

# Security
--------
The application uses API keys for user authentication. Before processing API requests, it validates the API key provided in the request header against the keys stored in the users table in the database. If the API key is invalid or not provided, it raises an HTTPException with status code 401.

The API keys are hashed using the SHA-256 algorithm for secure storage. SHA-256 (Secure Hash Algorithm 256 bit) is a cryptographic hash function that produces a 256-bit (32-byte) hash value. It's commonly used in security applications and protocols.


# Prerequisites
-------------

Before you begin, ensure you have met the following requirements:

*   You have installed Python 3.6+.
*   You have installed PostgreSQL.
*   You have installed FastAPI and hypercorn. You can install them with pip:
```
pip install fastapi

pip install hypercorn
```
# Usage
-----

To use the FastAPI application, follow these steps:
1.  Clone this repository using git clone:
```
git clone https://github.com/vedantgarode/FastAPI
```
2. Go to the app directory and install all the dependancy 
```
pip install -r requirements.txt
```
3.  Run the application using Uvicorn:
```
hypercorn main:app --reload
```
4. Open your web browser and navigate to [http://localhost:8000/](http://localhost:8000/). The application will serve an index.html page from the 'static' directory. For API documentation, navigate to [http://localhost:8000/docs](http://localhost:8000/docs). You will see the automatic interactive API documentation (provided by Swagger UI).

# Application Structure
---------------------

The application is structured as follows:

*   The application is initiated with an instance of FastAPI.
*   At startup, the application creates items and users tables in the database if they do not exist.
*   The application provides several API endpoints:

### 🐥GET /generate\_key/

This endpoint generates a new API key for a user.

Request Body:
```
{
    "user\_name": "johndoe"
}
 ```           

#### Example Request:
```
curl -X GET "http://localhost:8000/generate\_key/?user\_name=johndoe"
   ```         

#### Example Response:
```
{
    "status": "User Added",
    "APIKey": {
        "key": "abcdefghijklmnopqrstuvwxyz",
        "username": "johndoe"
    }
}
   ```         

### 🐥POST /add\_item/

This endpoint creates a new item in the 'items' table.

Request Body:
```
{
    "item": {
        "name": "item1",
        "price": 10
    }
}
   ```         

#### Example Request:
```
curl -X POST "http://localhost:8000/add\_item/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\\"name\\":\\"item1\\",\\"price\\":10}"
```       

#### Example Response:
```
{
    "status": "Item created",
    "id": 1
}
  ```         

### 🐥GET /get\_items/

This endpoint retrieves all items from the 'items' table.

#### Example Request:
```
curl -X GET "http://localhost:8000/get\_items/"
    ```        

#### Example Response:
```
{
    "items": \[
        {
            "id": 1,
            "name": "item1",
            "price": 10
        },
        {
            "id": 2,
            "name": "item2",
            "price": 20
        }
    \]
}
    ```        

### 🐥GET /get\_item/{item\_id}

This endpoint retrieves a specific item by ID from the 'items' table.

#### Example Request:
```
curl -X GET "http://localhost:8000/get\_item/1"
   ```         

#### Example Response:
```
{
    "item": \[
        {
            "id": 1,
            "name": "item1",
            "price": 10
        }
    \]
}
            
```
### 🐥PUT /item/{item :Item}

This endpoint updates a specific item by ID in the 'items' table.

Request Body:
```
{
    "item": {
        "name": "item2",
        "price": 20,
        "id": 2
    }
}
  ```          

#### Example Request:
```
curl -X PUT "http://localhost:8000/item/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\\"name\\":\\"item2\\",\\"price\\":20}"
            
```
#### Example Response:
```
{
    "status": "Item updated"
}
```         

### 🐥DELETE /items/{item\_id}

This endpoint deletes a specific item by ID from the 'items' table.

#### Example Request:
```
curl -X DELETE "http://localhost:8000/items/1"
   ```         

#### Example Response:
```
{
    "status": "Item deleted"
}
```        



Examples [Hosted on Railway.io]
--------

Here are some examples of how to use the Hosted API:
**[ Please Do not Spam Request !! It is on Free Plan]**

*   Generate a new API key for a user:
```
curl -X GET "http://roundhouse.proxy.rlwy.net:50234/generate\_key/?user\_name=johndoe"
```        

*   Add a new item:
```
curl -X POST "http://roundhouse.proxy.rlwy.net:50234/add\_item/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\\"name\\":\\"item1\\",\\"price\\":10}"
            
```
*   Get all items:
  ```
curl -X GET "http://roundhouse.proxy.rlwy.net:50234/get\_items/"
            
```
*   Get a specific item:
```
curl -X GET "http://roundhouse.proxy.rlwy.net:50234/get\_item/1"
```       

*   Update an item:
```
curl -X PUT "http://roundhouse.proxy.rlwy.net:50234/item/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\\"name\\":\\"item2\\",\\"price\\":20}"
```        

*   Delete an item:
```
curl -X DELETE "http://roundhouse.proxy.rlwy.net:50234/items/1"
```
