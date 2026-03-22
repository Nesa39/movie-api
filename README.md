# movie-api-git
# 🎬 Movie API (Django REST Framework)

## 🚀 Project Overview

This is a Movie API built using Django REST Framework.
It allows users to manage movies and directors with full CRUD operations.

---

## ⚙️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite

---

## 🔑 Features

* Create, Read, Update, Delete Movies
* Director management
* RESTful APIs
* Pagination & Filtering

---


## 🔐 Authentication (JWT)

This API uses JWT authentication.

### Get Token

POST `/api/token/`

### Refresh Token

POST `/api/token/refresh/`

Add token in headers:
Authorization: Bearer <your_token>

---

## 🔎 Filtering & Search

You can filter movies using query params:

* `/movies/?title=avatar`
* `/movies/?director=1`

### Supports:

* Search
* Filtering
* Pagination


## 🛠️ Setup Instructions

```bash
git clone https://github.com/Nesa39/movie-api.git
cd movie-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 📡 API Endpoints

* `/movies/`
* `/directors/`

---

## 📌 Author

Nesa Mani
