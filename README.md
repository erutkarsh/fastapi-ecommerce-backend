# fastapi-ecommerce-backend
Built a FastAPI-based e-commerce backend with JWT authentication, SQLAlchemy ORM, and secure password hashing using bcrypt.

# 🛒 E-Commerce Backend API (FastAPI)

## 🚀 Features
- User Registration & Login
- JWT Authentication
- Password Hashing (bcrypt)
- Protected Routes
- SQLite Database (SQLAlchemy)

## 🧱 Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- Passlib (bcrypt)
- Python-JOSE (JWT)

## 🔐 Authentication Flow
- Register → Store hashed password
- Login → Generate JWT token
- Access protected routes using token

## 📦 API Endpoints

### User
- POST /users/register
- POST /users/login
- GET /users/ (Protected)

## ▶️ Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
