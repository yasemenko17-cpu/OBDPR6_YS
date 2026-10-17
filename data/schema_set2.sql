-- Схема набору 2: Магазин. PostgreSQL 18.
-- Файл створює таблиці й наповнює їх початковими даними. Виконуйте його в ПОРОЖНІЙ схемі.

CREATE TABLE category (
    id        integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name      varchar(100) NOT NULL UNIQUE,
    parent_id integer REFERENCES category (id)
);

CREATE TABLE product (
    id      integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    sku  varchar(20) NOT NULL UNIQUE,
    title varchar(200) NOT NULL,
    category_id   integer NOT NULL REFERENCES category (id),
    price numeric(10,2) NOT NULL CHECK (price >= 0),
    stock   integer NOT NULL DEFAULT 0 CHECK (stock >= 0)
);

CREATE TABLE customer (
    id      integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name varchar(150) NOT NULL,
    city varchar(60) NOT NULL
);

CREATE TABLE purchase (
    id         integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id integer NOT NULL REFERENCES customer (id),
    product_id   integer NOT NULL REFERENCES product (id),
    quantity    integer NOT NULL DEFAULT 1 CHECK (quantity > 0),
    ordered_on   date NOT NULL,
    shipped_on date
);

-- Початкові дані

INSERT INTO category (name, parent_id) VALUES
    ('Продукти', NULL),
    ('Бакалія', 1),
    ('Молочні вироби', 1),
    ('Крупи', 2),
    ('Макарони', 2),
    ('Побутова хімія', NULL),
    ('Прибирання', 6),
    ('Для кухні', 7);

INSERT INTO product (sku, title, category_id, price, stock) VALUES
    ('SKU-0001', 'Молоко 2,5% 1 л', 3, 38.50, 40),
    ('SKU-0002', 'Спагеті 500 г', 5, 42.90, 25),
    ('SKU-0003', 'Гречка 1 кг', 4, 64.00, 30),
    ('SKU-0004', 'Рис довгозернистий 1 кг', 4, 58.50, 0),
    ('SKU-0005', 'Пенне 500 г', 5, 41.00, 18),
    ('SKU-0006', 'Сир кисломолочний 350 г', 3, 72.00, 12),
    ('SKU-0007', 'Вівсянка 800 г', 4, 36.80, 22),
    ('SKU-0008', 'Пшоно 1 кг', 4, 33.00, 15),
    ('SKU-0009', 'Фузилі 500 г', 5, 43.50, 9),
    ('SKU-0010', 'Лазанья 500 г', 5, 55.00, 6),
    ('SKU-0011', 'Засіб для посуду 500 мл', 8, 79.00, 14),
    ('SKU-0012', 'Губки для посуду 5 шт', 8, 24.00, 50),
    ('SKU-0013', 'Порошок пральний 3 кг', 7, 289.00, 8),
    ('SKU-0014', 'Рідке мило 300 мл', 7, 47.00, 20);

INSERT INTO customer (full_name, city) VALUES
    ('Ольга Мазур', 'Київ'),
    ('Богдан Кириленко', 'Одеса'),
    ('Лариса Гнатюк', 'Київ'),
    ('Роман Яковенко', 'Дніпро'),
    ('Оксана Давиденко', 'Одеса'),
    ('Максим Остапчук', 'Київ'),
    ('Віра Шаповал', 'Дніпро'),
    ('Артем Лозинський', 'Одеса'),
    ('Галина Романюк', 'Київ'),
    ('Станіслав Пилипенко', 'Дніпро');

INSERT INTO purchase (customer_id, product_id, quantity, ordered_on, shipped_on) VALUES
    (1, 1, 1, '2025-02-01', '2025-02-15'),
    (1, 3, 1, '2025-03-01', '2025-03-20'),
    (1, 10, 1, '2025-07-05', NULL),
    (2, 6, 1, '2025-03-10', NULL),
    (2, 1, 2, '2025-04-02', '2025-04-20'),
    (3, 1, 1, '2025-03-15', '2025-04-01'),
    (3, 8, 2, '2025-04-02', '2025-04-20'),
    (3, 11, 1, '2025-05-10', '2025-05-30'),
    (4, 3, 1, '2025-04-05', NULL),
    (4, 10, 1, '2025-04-18', '2025-05-02'),
    (5, 7, 1, '2025-05-01', '2025-05-12'),
    (5, 11, 1, '2025-05-03', NULL),
    (5, 13, 1, '2025-06-02', '2025-06-20'),
    (6, 2, 1, '2025-05-20', NULL),
    (6, 5, 1, '2025-06-01', '2025-06-15'),
    (6, 8, 1, '2025-06-18', '2025-06-30'),
    (7, 6, 2, '2025-06-10', NULL),
    (7, 7, 1, '2025-06-12', '2025-06-28'),
    (8, 5, 1, '2025-06-20', NULL),
    (8, 8, 1, '2025-07-01', NULL),
    (9, 13, 2, '2025-07-10', NULL),
    (9, 1, 1, '2025-07-12', NULL);
