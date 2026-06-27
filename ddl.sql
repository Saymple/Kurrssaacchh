-- Таблица пользователей (стандартная модель Django)
CREATE TABLE users_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(150) UNIQUE NOT NULL,
    email VARCHAR(254),
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    is_active BOOLEAN NOT NULL DEFAULT 1,
    is_staff BOOLEAN NOT NULL DEFAULT 0
);

-- Таблица объявлений
CREATE TABLE cars_car (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INTEGER,
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    mileage INTEGER CHECK (mileage >= 0),
    body_type VARCHAR(50),
    description TEXT,
    image VARCHAR(100),
    created_at DATETIME NOT NULL,
    seller_id INTEGER NOT NULL,
    FOREIGN KEY (seller_id) REFERENCES users_user(id) ON DELETE CASCADE
);

-- Индекс для быстрого поиска по продавцу
CREATE INDEX cars_car_seller_id ON cars_car(seller_id);

-- Индекс для быстрого поиска по марке
CREATE INDEX cars_car_brand ON cars_car(brand);

-- Таблица избранного
CREATE TABLE favorites_favorite (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    car_id INTEGER NOT NULL,
    added_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users_user(id) ON DELETE CASCADE,
    FOREIGN KEY (car_id) REFERENCES cars_car(id) ON DELETE CASCADE,
    UNIQUE (user_id, car_id)
);

-- Индекс для быстрого поиска избранного пользователя
CREATE INDEX favorites_favorite_user_id ON favorites_favorite(user_id);
