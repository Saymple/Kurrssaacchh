# AutoMarket — Веб-приложение для продажи подержанных автомобилей

Курсовой проект по дисциплине «Технология разработки программного обеспечения»  
Траектория **А**: Full-stack Django (классический подход)

---

## Технологический стек

| Слой | Технологии |
|------|-----------|
| Backend | Django 6.0, Django ORM |
| Frontend | Django Templates, Bootstrap 5, JavaScript (AJAX) |
| БД | SQLite (разработка) |
| Аутентификация | Сессионная (Django sessions) |
| Сервер | Встроенный WSGI-сервер Django |

---

## Быстрый старт (локально)

```bash
git clone https://github.com/Saymple/Kurrssaacchh.git
cd Kurrssaacchh
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Доступные адреса

| Адрес | Назначение |
|-------|-----------|
| `http://127.0.0.1:8000/` | Главная страница (лента объявлений) |
| `http://127.0.0.1:8000/admin/` | Django Admin |
| `http://127.0.0.1:8000/users/login/` | Вход в систему |
| `http://127.0.0.1:8000/users/register/` | Регистрация |

---

## Структура проекта

```
Kurrssaacchh/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── cars/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── users/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── favorites/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/
│   ├── base.html
│   ├── cars/
│   │   ├── list.html
│   │   ├── detail.html
│   │   ├── create.html
│   │   └── update.html
│   └── users/
│       ├── register.html
│       ├── login.html
│       └── profile.html
├── static/
│   ├── css/style.css
│   └── js/main.js
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

## Основной функционал

### Гости (неавторизованные)
- Просмотр ленты объявлений с пагинацией
- Фильтрация по марке и диапазону цен
- Поиск по марке, модели, описанию
- Просмотр детальной информации об автомобиле
- Регистрация и вход

### Пользователи (авторизованные)
- Создание, редактирование, удаление своих объявлений
- Добавление/удаление в избранное (AJAX)
- Управление профилем

### Администратор
- Управление всеми объявлениями через Django Admin
- Управление пользователями

---

## AJAX-эндпоинты

| Метод | URL | Описание | Авторизация |
|-------|-----|----------|-------------|
| POST | `/favorites/toggle/` | Добавление/удаление из избранного | Да |
| GET | `/api/search/` | Поиск объявлений (JSON) | Нет |

### Формат ответа

```json
{ "status": "added" }
{ "status": "removed" }
```

### Пример использования

```javascript
fetch('/favorites/toggle/', {
    method: 'POST',
    headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: 'car_id=1'
})
.then(r => r.json())
.then(data => {
    if (data.status === 'added') {
        // обновить интерфейс
    }
});
```

---

## Запуск тестов

```bash
python manage.py test cars
python manage.py test users
python manage.py test favorites
```

---

## Статистика разработки

- Всего коммитов: 1
- Дата создания: 25.06.2026
- Репозиторий: https://github.com/Saymple/Kurrssaacchh

---

## Перспективы развития

- Комментарии к объявлениям
- Чат между продавцом и покупателем
- Подключение PostgreSQL
- Верификация пользователей
- Расширенная фильтрация

---

## Автор

**Белоусов Артем Вадимович**  
Группа ПИЖ-б-о-24-1  
Направление 09.03.04 «Программная инженерия»  
СКФУ, 2026
