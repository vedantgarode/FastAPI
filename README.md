#FastAPI Application README
This is the README documentation for a FastAPI application that provides a simple API for managing Items and API keys for users. The application uses PostgreSQL as a database backend.

#Description
The application is built with FastAPI, a modern, fast web framework for building APIs with Python 3.6+ based on standard Python type hints. It features automatic interactive API documentation, easy to learn, and is highly scalable github.com.

This application has various functionalities including user authentication using API keys, CRUD operations for items, and automatic creation of database tables at startup.

#Prerequisites
Before you begin, ensure you have met the following requirements:

You have installed Python 3.6+.
You have installed PostgreSQL.
You have installed FastAPI and Uvicorn. You can install them with pip:
```
pip install fastapi
pip install "uvicorn[standard]"
```
#Usage
To use the FastAPI application, follow these steps:

Run the application using Uvicorn:
```
uvicorn main:app --reload
```
Open your web browser and navigate to http://localhost:8000/. The application will serve an index.html page from the 'static' directory.
For API documentation, navigate to http://localhost:8000/docs. You will see the automatic interactive API documentation (provided by Swagger UI).
#Application Structure
The application is structured as follows:

The application is initiated with an instance of FastAPI.
At startup, the application creates items and users tables in the database if they do not exist.
The application provides several API endpoints:
* `GET /`: Serves the `index.html` page from the 'static' directory.

* `GET /generate_key/`: Generates a new API key for a user. It raises an HTTPException if the username already exists.

* `POST /add_item/`: Creates a new item in the 'items' table. It requires an API key for authentication.

* `GET /get_items/`: Retrieves all items from the 'items' table. It requires an API key for authentication.

* `GET /get_item/{item_id}`: Retrieves a specific item by ID from the 'items' table. It requires an API key for authentication.

* `PUT /item/{item :Item}`: Updates a specific item by ID in the 'items' table. It requires an API key for authentication.

* `DELETE /items/{item_id}`: Deletes a specific item by ID from the 'items' table. It requires an API key for authentication.


#Security
The application uses API keys for user authentication. Before processing API requests, it validates the API key provided in the request header against the keys stored in the users table in the database. If the API key is invalid or not provided, it raises an HTTPException with status code 401.

Examples
Here are some examples of how to use the application:

<h2>Examples</h2>
        <p>Here are some examples of how to use the application:</p>
        <ul>
            <li>Generate a new API key for a user:</li>
        </ul>
        <div class="code">
            <pre>
curl -X GET "http://roundhouse.proxy.rlwy.net:50234/generate_key/?user_name=johndoe"
            </pre>
        </div>
        <ul start="2">
            <li>Add a new item:</li>
        </ul>
        <div class="code">
            <pre>
curl -X POST "http://roundhouse.proxy.rlwy.net:50234/add_item/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"item1\",\"price\":10}"
            </pre>
        </div>
        <ul start="3">
            <li>Get all items:</li>
        </ul>
        <div class="code">
            <pre>
curl -X GET "http://roundhouse.proxy.rlwy.net:50234/get_items/"
            </pre>
        </div>
        <ul start="4">
            <li>Get a specific item:</li>
        </ul>
        <div class="code">
            <pre>
curl -X GET "http://roundhouse.proxy.rlwy.net:50234/get_item/1"
            </pre>
        </div>
        <ul start="5">
            <li>Update an item:</li>
        </ul>
        <div class="code">
            <pre>
curl -X PUT "http://roundhouse.proxy.rlwy.net:50234/item/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"item2\",\"price\":20}"
            </pre>
        </div>
        <ul start="6">
            <li>Delete an item:</li>
        </ul>
        <div class="code">
            <pre>
curl -X DELETE "http://roundhouse.proxy.rlwy.net:50234/items/1"
            </pre>
        </div>
    </div>