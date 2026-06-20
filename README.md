
# 🚀 FastAPI JWT Authentication System

A secure and scalable authentication system built using **FastAPI**, featuring JWT-based authentication, user management, and **PostgreSQL database support**.

---

## 🔗 Live Demo

* 🌐 **Live API:** [FastAPI JWT Authentication System](https://fastapi-jwt-authentication-system.onrender.com?utm_source=chatgpt.com)
* 📄 **API Documentation (Swagger UI):** [API Docs](https://fastapi-jwt-authentication-system.onrender.com/docs?utm_source=chatgpt.com)
* 📦 **GitHub Repository:** [GitHub Repo](https://github.com/PavanSurisetti/FastAPI-JWT-Authentication-System?utm_source=chatgpt.com)

> ⚠️ Note: Hosted on Render free tier — initial response may be slow after inactivity.

---

## 🛠 Tech Stack

* **Backend Framework:** FastAPI
* **Authentication:** JWT (JSON Web Tokens)
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Validation:** Pydantic
* **Server:** Uvicorn
* **Deployment:** Render
* **Version Control:** Git & GitHub

---

## 💡 Features

* User registration and login system
* Secure JWT-based authentication
* Token-based access control
* Protected routes for authorized users
* Fast and high-performance REST API
* Auto-generated Swagger UI documentation
* PostgreSQL-backed persistent storage
* Production-ready deployment setup

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/PavanSurisetti/FastAPI-JWT-Authentication-System.git
cd FastAPI-JWT-Authentication-System
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install & Configure PostgreSQL

Make sure PostgreSQL is installed and running on your system:

* Create a new database (e.g., `fastapi_auth`)
* Create a database user with password
* Grant privileges to the user

Example local connection URL:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/fastapi_auth
```

---

### 5️⃣ Configure environment variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=postgresql://username:password@localhost:5432/fastapi_auth
```

---

### 6️⃣ Run the application

```bash
uvicorn main:app --reload
```

---

### 7️⃣ Open in browser

```
http://127.0.0.1:8000/docs
```

---

## 📂 Project Structure

```
FastAPI-JWT-Authentication-System/
├── main.py              # FastAPI app entry point
├── models.py           # Database models
├── schemas.py          # Pydantic schemas
├── auth.py             # JWT authentication logic
├── database.py         # PostgreSQL connection setup
├── requirements.txt    # Dependencies
├── .env                # Environment variables (not committed)
└── .gitignore
```

---

## 🔐 Authentication Flow

1. User registers with credentials
2. Password is hashed and stored in PostgreSQL
3. User logs in with credentials
4. Server generates JWT token
5. Token is used to access protected routes
6. Token validation happens on each request

---

## 🚀 Deployment

Deployed using **Render** with:

* FastAPI web service
* PostgreSQL database integration
* Environment variable configuration
* Auto deployment from GitHub
* Managed hosting for scalability

---

## 📈 Future Improvements

* Role-based access control (RBAC)
* Refresh tokens implementation
* OAuth2 login (Google/GitHub)
* Rate limiting & security enhancements
* Docker containerization
* Unit & integration testing

---

## 🤝 Contributing

Contributions are welcome:

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push and submit a pull request

---

## 📫 Contact

* GitHub: [PavanSurisetti](https://github.com/PavanSurisetti)
* LinkedIn: [Pavan Surisetti](https://www.linkedin.com/in/pavan-surisetti-b3281228b/)

---

## 📄 License

This project is licensed under the **MIT License**.
