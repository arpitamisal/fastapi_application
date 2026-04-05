# 📚 FastAPI Bookstore API

A simple **CRUD API** built using **FastAPI + SQLAlchemy + MySQL** to manage a bookstore database.

---

## 🚀 Features

- Create a new book 📖
- Get all books 📚
- Get a single book 🔍
- Update a book ✏️
- Delete a book ❌
- MySQL database integration using SQLAlchemy ORM
- Interactive API docs with Swagger UI

---

## 🛠️ Tech Stack

- **FastAPI** – Web framework  
- **SQLAlchemy** – ORM for database  
- **MySQL** – Database  
- **Pydantic** – Data validation  
- **Uvicorn** – ASGI server  

---

## 📁 Project Structure


fastapi_application/
│
├── main.py # FastAPI app (routes)
├── database.py # DB connection & session
├── model.py # SQLAlchemy models
├── create_table.py # Create DB tables
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-bookstore.git
cd fastapi-bookstore
```

###  2. Create virtual environment
python -m venv fastapi
source fastapi/bin/activate   # Mac
fastapi\Scripts\activate      # Windows
3. Install dependencies
pip install fastapi uvicorn sqlalchemy mysql-connector-python

### 4. Configure Database
Update your database.py:
```
MYSQL_USER = "root"
MYSQL_PASSWORD = "yourpassword"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DATABASE = "fastapidb"
```

Make sure the database exists in MySQL:
```
CREATE DATABASE fastapidb;
```

### 5. Create tables
python create_table.py

### 6. Run the server
```
uvicorn main:app --reload
```

## 📌 API Endpoints
➤ Create Book
POST /books
```
Request Body

{
  "title": "The Alchemist",
  "author": "Paulo Coelho",
  "publish_date": "1988"
}
```
➤ Get All Books
```
GET /books
```
➤ Get Book by ID
```
GET /books/{id}
```
➤ Update Book
```
PUT /books/{id}
```

Request Body
```
{
  "title": "Updated Title",
  "author": "Updated Author",
  "publish_date": "2024"
}
```
➤ Delete Book
```
DELETE /books/{id}
```

## 📖 API Documentation

After running the server, open:

👉 http://127.0.0.1:8000/docs

Swagger UI allows you to test all endpoints easily.

## ✅ Example Response
```
{
  "id": 1,
  "title": "The Alchemist",
  "author": "Paulo Coelho",
  "publish_date": "1988"
}
```

## 💡 Future Improvements
Add authentication (JWT)
Add pagination & filtering
Use Alembic for migrations
Deploy using Docker



