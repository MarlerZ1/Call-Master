#!/bin/bash

# Синхронизация Моделей с Базой Данных
python -c "from app.models.utils import create_db, init_db; create_db(); init_db()"

# Запуск приложения
exec python /app/app/main.py
