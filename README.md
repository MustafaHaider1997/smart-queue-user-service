# 🧑‍⚕️ Smart Queue - User Service

The **User Service** is one of the core microservices in the **Smart Queue Management System**, responsible for managing user authentication and registration using secure JWT-based mechanisms. This service provides RESTful APIs for user signup, login, and profile retrieval, and is built with **FastAPI** and **MongoDB** (via Azure CosmosDB with Mongo API).

---

## 🚀 Features

* 📝 **User Registration** – Signup with email and password (hashed using `bcrypt`)
* 🔐 **JWT Authentication** – Secure token-based login using `HS256`
* 🧾 **User Profile Access** – Retrieve current user info via token
* ✅ **MongoDB Atlas / Azure CosmosDB** – Hosted NoSQL backend
* 📦 **Docker-Ready** – Fully containerized via Docker
* 🌐 **Swagger UI** – API documentation available at `/docs`

---

## 🛠️ Tech Stack

* **Framework**: FastAPI (Python 3.12+)
* **Database**: MongoDB via Azure CosmosDB (with SCRAM-SHA-256)
* **Auth**: JWT (via `python-jose`)
* **Hashing**: bcrypt
* **Containerization**: Docker
* **Environment Management**: `.env` via `python-dotenv`

---

## 📁 Project Structure

```
smart-queue-user-service/
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI entrypoint
│   ├── auth.py               # JWT & password hashing
│   ├── database.py           # MongoDB client setup
│   ├── models.py             # Pydantic schemas
│   ├── routes/               # Route definitions (register, login, profile)
│   └── schemas.py            # Request/response models
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker image setup
├── docker-compose.yml        # Optional local dev orchestration
└── .env                      # Secrets and DB URI (should not be committed)
```

---

## 🔑 .env Configuration (Sample)

```env
MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256
JWT_SECRET=supersecretkey1234567890987654321!
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🐳 Docker Instructions

### 🔧 Build the Docker image

```bash
docker build -t smart-queue-user-service .
```

### ▶️ Run the container

```bash
docker run -p 8000:8000 --env-file .env smart-queue-user-service
```

---

## 📦 API Endpoints

| Method | Endpoint    | Description                             |
| ------ | ----------- | --------------------------------------- |
| POST   | `/register` | Register a new user                     |
| POST   | `/login`    | Authenticate and get token              |
| GET    | `/profile`  | Get current user profile (requires JWT) |

---

## 🔐 Usage (Example)

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "test123"}'
```

---

## 📄 License

This project is licensed under the MIT License.
