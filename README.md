# Real-Time Collaboration & Chat Platform

A full-stack real-time collaboration platform where users can create workspaces, manage members, communicate through channels, exchange messages in real time, and receive notifications.

The project is built with **React, FastAPI, WebSockets, PostgreSQL, SQLAlchemy, JWT authentication, and Redis**.

---

## 🚀 Features

### 🔐 Authentication & Security

* User registration
* User login
* JWT-based authentication
* Password hashing with bcrypt
* Protected API endpoints
* Active/inactive user support
* Role-based access control
* Admin and member roles

### 👥 User Management

* View authenticated user profile
* User roles
* Protected user endpoints
* Workspace membership

### 🏢 Workspaces

* Create workspaces
* List user's workspaces
* Workspace ownership
* Add members to workspaces
* Workspace member roles

### 💬 Channels

* Create channels inside workspaces
* Add users to channels
* Channel membership validation
* Protected channel access

### ⚡ Real-Time Communication

* WebSocket-based communication
* Real-time message broadcasting
* Typing indicators
* Online/offline presence tracking
* Channel-based connections

### 📨 Messages

* Send messages
* Store messages in PostgreSQL
* Retrieve channel message history
* Real-time message broadcasting

### 🔔 Notifications

* User notifications
* Read/unread notification status
* Mark notifications as read

### 🗄️ Data & Infrastructure

* PostgreSQL database
* SQLAlchemy ORM
* Redis integration
* Redis Pub/Sub support
* Pydantic schemas

### 🧪 Testing

* Pytest backend tests
* Authentication tests
* Protected endpoint tests
* API testing

### 🎨 Frontend

* React
* Vite
* Axios
* Responsive dashboard
* Login and registration pages
* Workspace management interface

---

# 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │       React UI       │
                         │      + Vite          │
                         └──────────┬───────────┘
                                    │
                              HTTP / Axios
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      FastAPI         │
                         │       Backend        │
                         └──────────┬───────────┘
                                    │
                ┌───────────────────┼───────────────────┐
                │                   │                   │
                ▼                   ▼                   ▼
        ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
        │ PostgreSQL   │    │  WebSockets  │    │    Redis     │
        │   Database   │    │ Real-Time    │    │ Pub/Sub      │
        └──────────────┘    └──────────────┘    └──────────────┘
```

---

# 🛠️ Tech Stack

## Frontend

* React
* Vite
* Axios
* JavaScript
* CSS

## Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* WebSockets

## Authentication

* JWT
* Python-JOSE
* Passlib
* bcrypt

## Database

* PostgreSQL

## Real-Time & Messaging

* WebSockets
* Redis
* Redis Pub/Sub

## Testing

* Pytest
* FastAPI TestClient

## Development Tools

* Git
* GitHub
* VS Code

---

# 📁 Project Structure

```text
real-time-collaboration-platform/
│
├── backend/
│   │
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   │       ├── auth.py
│   │   │       ├── channels.py
│   │   │       ├── health.py
│   │   │       ├── messages.py
│   │   │       ├── notifications.py
│   │   │       ├── users.py
│   │   │       ├── websocket.py
│   │   │       └── workspaces.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── dependencies.py
│   │   │   ├── redis_client.py
│   │   │   ├── rbac.py
│   │   │   └── security.py
│   │   │
│   │   ├── db/
│   │   │   ├── database.py
│   │   │   ├── models.py
│   │   │   ├── workspace_models.py
│   │   │   ├── channel_models.py
│   │   │   ├── channel_members.py
│   │   │   ├── message_models.py
│   │   │   └── notification_models.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── user.py
│   │   │   ├── workspace.py
│   │   │   ├── channel.py
│   │   │   └── message.py
│   │   │
│   │   ├── services/
│   │   │   └── pubsub.py
│   │   │
│   │   └── websocket/
│   │       └── manager.py
│   │
│   ├── tests/
│   │   └── test_auth.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   └── Dashboard.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── package.json
│   └── vite.config.js
│
├── .env.example
├── .gitignore
└── README.md
```

---

# ⚙️ Prerequisites

Make sure the following are installed:

* Python 3.10+
* Node.js
* npm
* PostgreSQL
* Redis
* Git

---

# 🔧 Backend Setup

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/real-time-collaboration-platform.git
```

Enter the project:

```bash
cd real-time-collaboration-platform
```

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install backend dependencies:

```powershell
pip install -r backend\requirements.txt
```

---

# 🗄️ PostgreSQL Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE collaboration_db;
```

The application expects PostgreSQL to be available on:

```text
localhost:5432
```

---

# 🔐 Environment Variables

Create a `.env` file based on `.env.example`.

Example:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/collaboration_db
SECRET_KEY=YOUR_SECRET_KEY
REDIS_URL=redis://localhost:6379/0
```

**Never commit your real `.env` file or credentials to GitHub.**

---

# ▶️ Run the Backend

From the project root:

```powershell
cd backend
```

Start FastAPI:

```powershell
uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🎨 Frontend Setup

Open another terminal:

```powershell
cd frontend
```

Install dependencies:

```powershell
npm install
```

Start the development server:

```powershell
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🧪 Running Tests

Go to the backend:

```powershell
cd backend
```

Run:

```powershell
pytest -v
```

The tests cover authentication and protected API functionality.

---

# 🔌 API Endpoints

Some of the main API endpoints include:

| Method | Endpoint                   | Description          |
| ------ | -------------------------- | -------------------- |
| GET    | `/`                        | API status           |
| GET    | `/health`                  | Health check         |
| POST   | `/auth/register`           | Register user        |
| POST   | `/auth/login`              | Login                |
| GET    | `/users/me`                | Current user         |
| POST   | `/workspaces`              | Create workspace     |
| GET    | `/workspaces`              | List workspaces      |
| POST   | `/workspaces/{id}/members` | Add workspace member |
| POST   | `/channels/{id}`           | Create channel       |
| POST   | `/messages/{id}`           | Create message       |
| GET    | `/messages/{id}`           | Message history      |
| GET    | `/notifications`           | Get notifications    |

---

# ⚡ WebSocket

Real-time channel communication is provided through WebSockets.

Endpoint:

```text
ws://127.0.0.1:8000/ws/channels/{channel_id}
```

The WebSocket layer supports real-time channel communication and events such as typing indicators.

---

# 🔄 Application Flow

```text
User
 │
 ▼
React Frontend
 │
 ├── Register
 │
 ├── Login
 │
 ▼
JWT Token
 │
 ▼
FastAPI Backend
 │
 ├── Authentication
 ├── Authorization
 ├── Workspaces
 ├── Channels
 ├── Messages
 └── Notifications
 │
 ├───────────────┐
 ▼               ▼
PostgreSQL      Redis
 │
 ▼
Persistent      Real-Time
Data            Messaging
```

---

# 🔒 Authentication Flow

```text
User
 │
 ▼
Login
 │
 ▼
FastAPI
 │
 ▼
Verify Password
 │
 ▼
Generate JWT
 │
 ▼
React stores token
 │
 ▼
Protected API Request
 │
 ▼
JWT Validation
 │
 ▼
Authenticated User
```

---

# 🧑‍💻 Roles

The platform supports:

### Admin

* Manage workspace resources
* Add members
* Administrative permissions

### Member

* Access assigned workspaces
* Participate in channels
* Send and receive messages

---

# 📸 Screenshots

Add screenshots here after capturing your final UI.

Example:

```markdown
## Login

![Login](docs/login.png)

## Registration

![Registration](docs/register.png)

## Dashboard

![Dashboard](docs/dashboard.png)

## API Documentation

![Swagger](docs/swagger.png)

## Real-Time Chat

![Real-Time Chat](docs/realtime-chat.png)
```

---

# 🚧 Future Improvements

Possible future improvements include:

* Direct messaging
* File sharing
* Message reactions
* Message editing and deletion
* Advanced notification system
* Fully authenticated WebSocket connections
* Redis-backed multi-instance WebSocket broadcasting
* Search across messages
* User profile management
* Email notifications
* Docker deployment
* Cloud deployment
* CI/CD improvements
* Automated frontend testing

---

# 🎯 Project Goals

This project was built to demonstrate practical experience with:

* Full-stack application development
* REST API development
* JWT authentication
* Role-based authorization
* Relational database design
* SQLAlchemy ORM
* WebSocket communication
* Real-time application architecture
* Redis Pub/Sub
* React frontend development
* Automated testing
* Git and GitHub workflows

---

# 📄 License

This project is intended for educational and portfolio purposes.
