# Analytics-Service
This service was created for storing and analyzing data. The backend was implemented using FastAPI, and the user interface is based on Streamlit. Data is loaded from a file and modified via the API.

## Project Structure

```text
Analytics-Service/
├── backend/                # FastAPI backend application files
│   ├── Dockerfile          # Dockerfile for the backend service
│   ├── requirements.txt    # Python dependencies for the backend
│   ├── main.py             # Backend main application code
│   └── data.csv            # Data storage file
├── frontend/               # Streamlit frontend application files
│   ├── Dockerfile          # Dockerfile for the frontend service
│   ├── requirements.txt    # Python dependencies for the frontend
│   └── app.py              # Frontend main application code
├── docker-compose.yml      # Docker Compose configuration for orchestrating services
├── pycodestyle.py          # Script for checking Python code style
└── README.md               # This README file
```

## Running the Application

This section provides instructions for running the application both locally (without Docker) and using Docker Compose.

### Local Setup (Without Docker)

#### Backend (FastAPI)

To run the backend service in Git Bash, execute the following commands sequentially:

1.  **Navigate to the backend directory:**
    ```bash
    cd task_02_service/backend/
    ```
2.  **Activate the virtual environment:**
    ```bash
    source ../../venv_backend/Scripts/activate
    ```
    *(Ensure `../../venv_backend` points to your actual virtual environment path)*
3.  **Run the Uvicorn script:**
    ```bash
    uvicorn main:app --reload --port 8000
    ```
4.  **Check service functionality:**
    Open your browser and go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger UI will open).
5.  **Check code style:**
    ```bash
    python pycodestyle.py backend/main.py --max-line-length=120
    ```

#### Frontend (Streamlit)

To run the frontend service in Git Bash, execute the following commands sequentially:

1.  **Navigate to the frontend directory:**
    ```bash
    cd task_02_service/frontend/
    ```
2.  **Activate the virtual environment:**
    ```bash
    source ../../venv_frontend/Scripts/activate
    ```
    *(Ensure `../../venv_frontend` points to your actual virtual environment path)*
3.  **Run the Streamlit script:**
    ```bash
    streamlit run app.py
    ```
4.  **Check service functionality:**
    Open your browser and go to: [http://localhost:8501](http://localhost:8501)
5.  **Check code style:**
    ```bash
    python pycodestyle.py frontend/app.py --max-line-length=120
    ```

---

### Docker Setup

#### Running with Docker Compose

1.  **Start Docker:** Ensure Docker Desktop is running.
2.  **Navigate to the `task_02_service` directory** (where `docker-compose.yml` is located).
3.  **Start the services:**
    ```bash
    docker-compose up --build -d
    ```
4.  **Stop the services:**
    ```bash
    docker-compose down
    ```

#### Service Endpoints (after `docker-compose up -d`)

*   **Backend API:** [http://localhost:8888/docs](http://localhost:8888/docs) (Swagger UI should open)
*   **Frontend:** [http://localhost:8889](http://localhost:8889) (Streamlit application should open)

---

## Инструкция по запуску

### Локальный запуск (без Docker)

#### Бэкенд (FastAPI)

Для запуска бэкенда в Git Bash последовательно введите команды:

1.  **Откройте директорию бэкенда:**
    ```bash
    cd task_02_service/backend/
    ```
2.  **Активируйте виртуальное окружение:**
    ```bash
    source ../../venv_backend/Scripts/activate
    ```
    *(Убедитесь, что `../../venv_backend` указывает на актуальный путь к вашему виртуальному окружению)*
3.  **Запустите сервис Uvicorn:**
    ```bash
    uvicorn main:app --reload --port 8000
    ```
4.  **Проверьте работоспособность сервиса:**
    Откройте браузер и перейдите по адресу: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (откроется Swagger UI).
5.  **Проверьте код на стиль:**
    ```bash
    python pycodestyle.py backend/main.py --max-line-length=120
    ```

#### Фронтенд (Streamlit)

Для запуска фронтенда в Git Bash последовательно введите команды:

1.  **Откройте директорию фронтенда:**
    ```bash
    cd task_02_service/frontend/
    ```
2.  **Активируйте виртуальное окружение:**
    ```bash
    source ../../venv_frontend/Scripts/activate
    ```
    *(Убедитесь, что `../../venv_frontend` указывает на актуальный путь к вашему виртуальному окружению)*
3.  **Запустите Streamlit:**
    ```bash
    streamlit run app.py
    ```
4.  **Проверьте работоспособность сервиса:**
    Откройте браузер и перейдите по адресу: [http://localhost:8501](http://localhost:8501)
5.  **Проверьте код на стиль:**
    ```bash
    python pycodestyle.py frontend/app.py --max-line-length=120
    ```

---

## Настройка Docker

### Запуск с Docker Compose

1.  **Запустите Docker:** Убедитесь, что Docker Desktop запущен.
2.  **Перейдите в директорию `task_02_service`** (где находится файл `docker-compose.yml`).
3.  **Запустите сервисы:**
    ```bash
    docker-compose up --build -d
    ```
    *   `--build` — для пересборки образов (особенно если были изменения в Dockerfile).
    *   `-d` — для запуска в фоновом режиме.
4.  **Остановка сервисов:**
    ```bash
    docker-compose down
    ```

### Конечные точки сервисов (после `docker-compose up -d`)

*   **Backend API:** [http://localhost:8888/docs](http://localhost:8888/docs) (откроется Swagger UI)
*   **Frontend:** [http://localhost:8889](http://localhost:8889) (откроется приложение Streamlit)

---