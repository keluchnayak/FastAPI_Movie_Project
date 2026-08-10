````markdown
# 🎬 Movie Explorer & Review Management System

<p align="center">
  <b>A full-stack movie management application built with FastAPI ⚡ and Streamlit 🚀</b>
</p>

<p align="center">
  REST API • CRUD Operations • Path Parameters • Query Parameters • Swagger • Streamlit
</p>

---

## ✨ Overview

**Movie Explorer & Review Management System** is a full-stack Python application that combines a FastAPI backend with a Streamlit frontend.

The project demonstrates how a frontend application communicates with a REST API to create, retrieve, search, update, and delete movie information.

The application was developed with a focus on understanding the fundamentals of:

- REST API development
- FastAPI routing
- Path parameters
- Query parameters
- CRUD operations
- JSON request/response handling
- Frontend ↔ Backend communication
- API testing with Swagger
- Git & GitHub workflow

---

## 🖥️ Application Preview

> 🎬 Movie Explorer

The Streamlit interface provides a simple dashboard for interacting with the movie API.

### Available Features

| Feature | Description |
|---|---|
| 🏠 Home | Project dashboard and overview |
| 🎬 View Movies | Display all available movies |
| 👁️ View Movie | Retrieve a movie using its ID |
| 🔎 Search Movies | Filter movies using query parameters |
| ➕ Add Movie | Add a new movie |
| ✏️ Update Movie | Update an existing movie |
| 🗑️ Delete Movie | Remove a movie |

---

# 🏗️ Project Architecture

```text
                    ┌──────────────────────┐
                    │      Streamlit       │
                    │      Frontend        │
                    └──────────┬───────────┘
                               │
                         HTTP Requests
                               │
                               ▼
                    ┌──────────────────────┐
                    │       FastAPI        │
                    │       Backend        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Movies Collection  │
                    │   Python List/Data   │
                    └──────────────────────┘
````

### Request Flow

```text
User
 ↓
Streamlit UI
 ↓
HTTP Request
 ↓
FastAPI Endpoint
 ↓
Movie Data Processing
 ↓
JSON Response
 ↓
Streamlit UI
```

---

# ⚡ Tech Stack

### Backend

* 🐍 Python 3.11
* ⚡ FastAPI
* 🚀 Uvicorn

### Frontend

* 🎨 Streamlit
* 🌐 Requests

### Development Tools

* 💻 Visual Studio Code
* 📖 Swagger UI
* 🔀 Git
* 🐙 GitHub

---

# 📁 Project Structure

```text
movie_project/
│
├── backend/
│   └── main.py
│
├── frontend/
│   ├── app.py
│   └── images/
│       └── bgbg.jpeg
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🔌 API Endpoints

## 🎬 Get All Movies

```http
GET /movies
```

Returns the complete movie collection.

---

## 👁️ Get Movie by ID

```http
GET /movies/{movie_id}
```

Uses a **Path Parameter** to retrieve a specific movie.

### Example

```http
GET /movies/1
```

### Concept

```python
@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
```

FastAPI extracts `movie_id` directly from the URL path.

---

## 🔎 Filter Movies

```http
GET /movies/filter
```

Uses optional **Query Parameters**.

Supported filters:

```text
genre
language
rating
```

### Example

```http
GET /movies/filter?genre=Sci-Fi&language=English&rating=9
```

Each parameter is optional.

For example:

```http
GET /movies/filter?genre=Sci-Fi
```

or:

```http
GET /movies/filter?rating=9
```

---

## ➕ Add Movie

```http
POST /movies
```

Accepts movie information through a JSON request body.

Example:

```json
{
    "id": 10,
    "movie_name": "Interstellar",
    "genre": "Sci-Fi",
    "language": "English",
    "rating": 9
}
```

---

## ✏️ Update Movie

```http
PUT /movies/{movie_id}
```

Updates the information of an existing movie.

Example:

```http
PUT /movies/10
```

---

## 🗑️ Delete Movie

```http
DELETE /movies/{movie_id}
```

Deletes a movie using its ID.

Example:

```http
DELETE /movies/10
```

---

# 🧩 CRUD Operations

The project implements the four fundamental CRUD operations:

```text
┌──────────────┬──────────┬─────────────────────┐
│ Operation    │ Method   │ Endpoint            │
├──────────────┼──────────┼─────────────────────┤
│ Create       │ POST     │ /movies             │
│ Read All     │ GET      │ /movies             │
│ Read One     │ GET      │ /movies/{movie_id}  │
│ Update       │ PUT      │ /movies/{movie_id}  │
│ Delete       │ DELETE   │ /movies/{movie_id}  │
└──────────────┴──────────┴─────────────────────┘
```

---

# 🛠️ Installation & Setup

## 1. Clone the repository

```bash
git clone https://github.com/keluchnayak/FastAPI_Movie_Project.git
```

Move into the project:

```bash
cd FastAPI_Movie_Project
```

---

## 2. Create a Virtual Environment

Python 3.11 is recommended for this project.

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

You should see:

```text
(.venv)
```

in your terminal.

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Running the Application

The project has two components:

```text
Backend  → FastAPI
Frontend → Streamlit
```

Both need to be running.

---

## ⚡ Start FastAPI Backend

From the project root:

```bash
uvicorn backend.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

# 📖 Swagger API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger allows you to:

* View available endpoints
* Enter path parameters
* Enter query parameters
* Send JSON request bodies
* Execute API requests
* Inspect JSON responses

---

# 🎨 Start Streamlit Frontend

Open another terminal.

Activate the virtual environment:

```powershell
.venv\Scripts\activate
```

Move into the frontend:

```powershell
cd frontend
```

Run:

```bash
streamlit run app.py
```

The application will normally open at:

```text
http://localhost:8501
```

---

# 🔗 Path Parameters vs Query Parameters

One of the important concepts demonstrated in this project is the difference between **path parameters** and **query parameters**.

## Path Parameter

Used to identify a specific resource.

```http
GET /movies/5
```

Here:

```text
5
```

is the `movie_id`.

FastAPI receives it through:

```python
@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
```

---

## Query Parameters

Used to filter or modify a request.

```http
GET /movies/filter?genre=Sci-Fi&rating=9
```

Here:

```text
genre = Sci-Fi
rating = 9
```

are query parameters.

---

# 🔄 Frontend ↔ Backend Communication

The Streamlit frontend communicates with FastAPI using the `requests` library.

Example:

```python
response = requests.get(
    f"{BASE_URL}/movies/{movie_id}"
)
```

The backend processes the request and returns JSON.

The frontend then displays the result to the user.

```text
Streamlit
    │
    │ HTTP GET
    ▼
FastAPI
    │
    │ JSON
    ▼
Streamlit
```

---

# 🧪 Testing

The API can be tested using:

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### Streamlit

```text
http://localhost:8501
```

### Browser

Simple GET endpoints can also be tested directly through a browser.

---

# 📌 Example Movie Object

The application works with movie objects containing fields such as:

```json
{
    "id": 1,
    "movie_name": "Interstellar",
    "genre": "Sci-Fi",
    "language": "English",
    "rating": 9
}
```

---

# 🎯 Learning Objectives

This project helped demonstrate practical implementation of:

```text
Python
   ↓
FastAPI
   ↓
REST API
   ↓
CRUD
   ↓
Path Parameters
   ↓
Query Parameters
   ↓
JSON
   ↓
Streamlit
   ↓
Frontend ↔ Backend Integration
   ↓
Git & GitHub
```

---

# 🚧 Current Limitations

The current implementation is intentionally simple and focuses on learning the fundamentals.

Movie data is maintained in memory rather than a persistent database.

Therefore:

```text
Application stops
      ↓
In-memory data is reset
```

---

# 🔮 Future Improvements

Possible future improvements include:

* 🗄️ Database integration
* 🔐 User authentication
* ⭐ Movie reviews
* ❤️ Favorites / watchlist
* 🔎 Advanced search
* 📊 Movie statistics
* 🖼️ Movie posters
* 📱 Improved responsive UI
* ☁️ Deployment
* 🧪 Automated testing

---

# 📚 What I Learned

Building this project helped me understand how a frontend and backend communicate through a REST API.

Some of the key concepts explored were:

> **Path parameters identify a specific resource, while query parameters allow flexible filtering of resources.**

I also learned how FastAPI automatically generates interactive Swagger documentation and how Streamlit can be used to create a frontend for a Python API.

---

# 👨‍💻 Author

**Kelu Chnayak**

Built as a learning project to explore:

```text
Python 🐍
FastAPI ⚡
Streamlit 🎨
REST APIs 🌐
Git 🔀
GitHub 🐙
```

---

## ⭐ If you found this project interesting

Feel free to explore the source code and follow the development journey.

**Built with Python. Built to learn. Built to improve.** 🎬

````

### One thing I'd do before committing this README

Your repository currently has a real GitHub URL, so the README can link directly to it. I'd also add a **real screenshot/GIF of your Streamlit interface** near the `Application Preview` section. That will make the GitHub repository dramatically more attractive than a text-only README.

For example:

```text
README
   ↓
🎬 Project screenshot
   ↓
Architecture
   ↓
Features
   ↓
API endpoints
   ↓
Setup
   ↓
GitHub
````
