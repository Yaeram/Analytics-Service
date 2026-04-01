# Analytics-Service
This service was created for storing and analyzing data. The backend was implemented using FastAPI, and the user interface is based on Streamlit. Data is loaded from a file and modified via the API.

# Brief instructions / Краткая инструкция

# Backend

To launch the backend in git bash, enter the following commands: cd task_02_service/backend/ - open the source directory venv_backend/Scripts/activate - run the uvicorn script main:app --reload --port 8000 - start the service - follow the link to check the service's functionality: http://127.0.0.1:8000/docs - check the code for style: python pycodestyle.py backend/main.py --max-line-length=120

# Frontend

To launch the frontend in git bash, enter the following commands: cd task_02_service/frontend/ - open the source directory venv_frontend/Scripts/activate - run the streamlit script run app.py - start the service - follow the link to check the service's functionality: http://localhost:8501 - check the code for style: python pycodestyle.py frontend/app.py --max-line-length=120

# Docker:

Start Docker: docker-compose up --build -d (from the task_02_service directory) To stop: docker-compose down

Backend API: http://localhost:8888/docs (Swagger UI should open). Frontend: http://localhost:8889 (Streamlit app should open).

# Backend

Для запуска backend в git bash ввести последовательно команды: cd task_02_service/backend/ - открытие директории source venv_backend/Scripts/activate -запуск скрипта uvicorn main:app --reload --port 8000 - запуск сервиса перейти по ссылкедля проверки работоспособности сервиса: http://127.0.0.1:8000/docs для проверки кода на стиль: python pycodestyle.py backend/main.py --max-line-length=120

# Frontend

Для запуска frontend в git bash ввести последовательно команды: cd task_02_service/frontend/ - открытие директории source venv_frontend/Scripts/activate - запуск скрипта streamlit run app.py - запуск сервиса перейти по ссылкедля проверки работоспособности сервиса: http://localhost:8501 для проверки кода на стиль: python pycodestyle.py frontend/app.py --max-line-length=120

# Docker:

Запуск Docker - : docker-compose up --build -d (из директории task_02_service) Для остановки - : docker-compose down

Backend API: http://localhost:8888/docs (должен открыться Swagger UI). Frontend: http://localhost:8889 (должно открыться Streamlit приложение).

# More detailed instructions / Более подробная инструкция

# EgorKryuchkov-Service_tasks1-3
This repository was created for tasks 1-3
README.md
markdown

# Energy Consumption & Price Dashboard

This project is a web service designed to manage and visualize energy consumption and pricing data. It consists of a backend (FastAPI) and a frontend (Streamlit), both containerized using Docker.

## Project Structure

task_02/ ├── backend/ # FastAPI backend application ├── frontend/ # Streamlit frontend application ├── docker-compose.yml # Docker orchestration configuration └── README.md # This file


## Prerequisites
- Docker Desktop installed and running.
- Git (optional, for cloning).

## Dockerization & Deployment

This project uses Docker Compose to orchestrate the backend and frontend services.

### Building the Docker Images
To build the images for both services from scratch, run the following command in the project root directory:

```bash
docker-compose build

Running the Service

To start both containers (backend and frontend) in the background, run:
bash

docker-compose up -d

Stopping the Service

To stop and remove the containers, run:
bash

docker-compose down

How to Use the Service

Once the containers are running, you can access the services via your web browser:

1. Frontend (User Interface)

Access the dashboard at: http://localhost:8889

Features:

    Data Table: View all current energy records in an interactive table.
    Charts: Automatically generated line charts visualizing “Energy Consumption Dynamics” and “Energy Price Dynamics” for both European and Siberian regions.
    Add New Record:
        Fill in the form with Timestamp (format: YYYY-MM-DD HH:MM:SS), Consumption values, and Price values.
        Click the “Add Record” button.
        The page will refresh, and the new data will appear in the table and charts.
    Delete Record:
        Enter the unique ID of the record you wish to delete in the “Delete Record” section.
        Click the “Delete Record” button.
        The record will be removed from the database, and the page will refresh.

2. Backend (API Documentation)

Access the interactive API documentation (Swagger UI) at: http://localhost:8888/docs

You can use this interface to test API endpoints (GET, POST, DELETE) directly without using the UI.
Troubleshooting

    Docker Error: If you see an error related to dockerDesktopLinuxEngine, ensure Docker Desktop is launched and fully running.
    Data Persistence: The data.csv file is mounted as a volume. Any data added or deleted through the UI will be saved in backend/data.csv on your host machine.
    Linter/Code Style: The code conforms to PEP8 standards. You can verify this using the provided pycodestyle.py script:
    bash

    python pycodestyle.py <path_to_script> --max-line-length=120

......

Этот проект представляет собой веб-сервис для управления и визуализации данных о потреблении энергии и ценах. Он состоит из бэкенда (FastAPI) и фронтенда (Streamlit), оба из которых контейнеризированы с помощью Docker.

##Структура проекта

```text
task_02/
├── backend/            # FastAPI бэкенд приложение
├── frontend/           # Streamlit фронтенд приложение
├── docker-compose.yml  # Конфигурация оркестрации Docker
├── README.md           # Этот файл
└── pycodestyle.py      # Файл для проверки стилей кода

##Предварительные требования

    Установленный и запущенный Docker Desktop.
    Git (опционально, для клонирования репозитория).

##Контейнеризация и развертывание

Проект использует Docker Compose для оркестрации бэкенд и фронтенд сервисов.
Сборка Docker-образов

Чтобы собрать образы для обоих сервисов с нуля, выполните следующую команду в корневой директории проекта:
bash

docker-compose build

##Запуск сервиса

Чтобы запустить оба контейнера (бэкенд и фронтенд) в фоновом режиме, выполните:
bash

docker-compose up -d

##Остановка сервиса

Чтобы остановить и удалить контейнеры, выполните:
bash

docker-compose down

##Инструкция по использованию сервиса

После того как контейнеры будут запущены, вы можете получить доступ к сервисам через ваш веб-браузер:

##1. Фронтенд (Пользовательский интерфейс)

Панель мониторинга доступна по адресу: http://localhost:8889

Функционал:

    Таблица данных: Просмотр всех текущих записей о потреблении энергии в интерактивной таблице.
    Графики: Автоматически сгенерированные линейные графики, визуализирующие “Динамику потребления энергии” и “Динамику цен на энергию” как для европейской, так и для сибирской части России.
    Добавление новой записи:
        Заполните форму, указав Timestamp (формат: ГГГГ-ММ-ДД ЧЧ:ММ:СС), значения Consumption (потребление) и Price (цены).
        Нажмите кнопку “Add Record”.
        Страница обновится, и новые данные появятся в таблице и на графиках.
    Удаление записи:
        Введите уникальный ID записи, которую хотите удалить, в разделе “Delete Record”.
        Нажмите кнопку “Delete Record”.
        Запись будет удалена из базы данных, и страница обновится.

##2. Бэкенд (API документация)

Интерактивная документация API (Swagger UI) доступна по адресу: http://localhost:8888/docs

Вы можете использовать этот интерфейс для тестирования API эндпоинтов (GET, POST, DELETE) напрямую, без использования UI.

##Ошибка Docker: 
    Если вы видите ошибку, связанную с dockerDesktopLinuxEngine, убедитесь, что Docker Desktop запущен и полностью готов к работе.
    Сохранение данных: Файл data.csv монтируется как volume. Любые данные, добавленные или удаленные через UI, будут сохранены в файле backend/data.csv на вашем компьютере.

##Стиль кода:
    Код соответствует стандартам PEP8. Вы можете проверить это с помощью предоставленного скрипта pycodestyle.py:

    python pycodestyle.py <путь_к_скрипту> --max-line-length=120

