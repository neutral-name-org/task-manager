# 📋 Task Manager REST API

This project is a simple Task Manager REST API built using Python (Flask) and containerized with Docker. It allows you to manage tasks with the following features:

- ✅ Create new tasks
- 📄 List all tasks
- 🔍 View individual task details
- ☑️ Mark tasks as done
- 🔎 Search tasks by title or description
- 📊 Order tasks by a specified field

## 🚀 Getting Started

### Prerequisites
- Docker installed on your machine

### Installation and Running

1. **Build the Docker Image**
   ```bash
   docker build -t task-api .
   ```

2. **Run the Container**
   ```bash
   docker run -p 5000:5000 task-api
   ```
   The API will be available at: http://localhost:5000

## 📝 API Endpoints

- **Create a Task**
  - **POST** `/tasks`
  - **Body**: `{ "title": "Your Task Title", "description": "Optional task description", "due_date": "2023-12-31" }`

- **List All Tasks**
  - **GET** `/tasks`
  - **Query Parameters**:
    - `search`: Filter tasks by title or description
    - `order_by`: Sort tasks by a specified field (e.g., 'id', 'title', 'due_date')

- **Get Task Details**
  - **GET** `/tasks/<task_id>`

- **Mark Task as Done**
  - **POST** `/tasks/<task_id>/done`

## 📦 Project Structure

- `app/`
  - `main.py`: Defines the API routes and initializes the Flask application.
  - `tasks.py`: Contains the `TaskManager` class for managing tasks.

- `Dockerfile`: Instructions for building the Docker image.
- `requirements.txt`: Lists the Python dependencies.

## 📌 Note

The app uses an in-memory dictionary to store tasks, so all data will reset when the server restarts.

