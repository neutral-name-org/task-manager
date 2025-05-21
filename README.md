📋 Task API (Docker + Python + Flask)

This project is a simple Task Manager REST API built using Python (Flask) and containerized with Docker. It lets you:
 •   ✅ Create new tasks
 •   📄 List all tasks
 •   🔍 View individual task details
 •   ☑️ Mark tasks as done

 The app uses an in-memory dictionary to store tasks — so all data will reset when the server restarts.

 ---

 🚀 Getting Started

1. Build the Docker Image
`docker build -t task-api .`

2. Run the container
`docker run -p 5000:5000 task-api`
The API will be available at: http://localhost:5000

