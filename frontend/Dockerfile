# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
# ИЗМЕНЕНИЕ: Убрали префикс "frontend/"
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
# ИЗМЕНЕНИЕ: Убрали префикс "frontend/"
COPY app.py .

# Порт, который слушает Streamlit
EXPOSE 8501

# Переменная окружения для бэкенда
ENV BACKEND_URL=http://backend:8888

# Команда запуска
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.headless", "true", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false"]