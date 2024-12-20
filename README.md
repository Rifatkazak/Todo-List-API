# RESTful To-Do List API

A simple RESTful API for managing a to-do list with user authentication and CRUD operations. This project is designed to help you learn and implement key concepts like RESTful API design, user authentication, database management, and error handling in Python using Flask.

---

## Features

- **User Authentication**:
  - User registration with secure password hashing.
  - Login endpoint with JWT (JSON Web Token) authentication.
- **CRUD Operations**:
  - Create, read, update, and delete tasks in a to-do list.
- **Database**:
  - SQLite database to store user and to-do list data.
- **Security**:
  - Token-based authentication for secure access to endpoints.
  - Input validation to prevent invalid data submissions.
- **Error Handling**:
  - Proper error messages for unauthorized access, missing data, and more.
- **Extensible Design**:
  - Pagination and filtering can be easily added to the to-do list.

---

## Endpoints

### User Authentication
| Method | Endpoint       | Description               |
|--------|----------------|---------------------------|
| POST   | `/auth/register` | Register a new user.      |
| POST   | `/auth/login`    | Login and get a JWT token.|

### To-Do List Management
| Method | Endpoint          | Description                                   |
|--------|-------------------|-----------------------------------------------|
| POST   | `/api/todos`      | Create a new to-do item.                      |
| GET    | `/api/todos`      | Get all to-do items for the authenticated user.|
| PUT    | `/api/todos/<id>` | Update a specific to-do item.                 |
| DELETE | `/api/todos/<id>` | Delete a specific to-do item.                 |

---

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Authentication**: JSON Web Tokens (JWT)

---

## Requirements

- Python 3.8 or higher
- pip (Python package manager)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/todo-api.git
   cd todo-api

