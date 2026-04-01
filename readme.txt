Простой проект по взаимодействию с планировщиком задач.
Создайте новый запрос

Выберите метод (GET, POST, PUT, DELETE)

Введите URL: http://localhost:8000/tasks/

Для POST/PUT добавьте Body → raw → JSON

Нажмите Send


Структура папок:

├── main.py
├── routers/
│   ├── __init__.py
│   └── task.py
└── schemas/
    ├── __init__.py
    └── task.py