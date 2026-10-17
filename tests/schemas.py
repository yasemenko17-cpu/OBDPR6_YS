"""Схеми й початкові дані трьох наборів (збігаються з файлами data/schema_setN.sql)."""

SCHEMAS = {1: '-- Схема набору 1: Бібліотека. PostgreSQL 18.\n'
    '-- Файл створює таблиці й наповнює їх початковими даними. Виконуйте його в ПОРОЖНІЙ схемі.\n'
    '\n'
    'CREATE TABLE genre (\n'
    '    id        integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,\n'
    '    name      varchar(100) NOT NULL UNIQUE,\n'
    '    parent_id integer REFERENCES genre (id)\n'
    ');\n'
    '\n'
    'CREATE TABLE book (\n'
    '    id      integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,\n'
    '    isbn  varchar(20) NOT NULL UNIQUE,\n'
    '    title varchar(200) NOT NULL,\n'
    '    genre_id   integer NOT NULL REFERENCES genre (id),\n'
    '    price numeric(10,2) NOT NULL CHECK (price >= 0),\n'
    '    copies   integer NOT NULL DEFAULT 0 CHECK (copies >= 0)\n'
    ');\n'
    '\n'
    'CREATE TABLE reader (\n'
    '    id      integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,\n'
    '    full_name varchar(150) NOT NULL,\n'
    '    city varchar(60) NOT NULL\n'
    ');\n'
    '\n'
    'CREATE TABLE loan (\n'
    '    id         integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,\n'
    '    reader_id integer NOT NULL REFERENCES reader (id),\n'
    '    book_id   integer NOT NULL REFERENCES book (id),\n'
    '    copies    integer NOT NULL DEFAULT 1 CHECK (copies > 0),\n'
    '    loaned_on   date NOT NULL,\n'
    '    returned_on date\n'
    ');\n'
    '\n'
    '-- Початкові дані\n'
    '\n'
    'INSERT INTO genre (name, parent_id) VALUES\n'
    "    ('Художня література', NULL),\n"
    "    ('Проза', 1),\n"
    "    ('Поезія', 1),\n"
    "    ('Роман', 2),\n"
    "    ('Повість', 2),\n"
    "    ('Наукова література', NULL),\n"
    "    ('Історія', 6),\n"
    "    ('Історія України', 7);\n"
    '\n'
    'INSERT INTO book (isbn, title, genre_id, price, copies) VALUES\n'
    "    ('9786170000011', 'Кобзар', 3, 320.00, 5),\n"
    "    ('9786170000028', 'Тіні забутих предків', 5, 210.50, 0),\n"
    "    ('9786170000035', 'Захар Беркут', 4, 185.00, 3),\n"
    "    ('9786170000042', 'Місто', 4, 260.00, 0),\n"
    "    ('9786170000059', 'Intermezzo', 5, 150.00, 2),\n"
    "    ('9786170000066', 'Лісова пісня', 3, 175.75, 7),\n"
    "    ('9786170000073', 'Тигролови', 4, 230.00, 1),\n"
    "    ('9786170000080', 'Маруся', 4, 140.00, 4),\n"
    "    ('9786170000097', 'Fata Morgana', 5, 199.90, 1),\n"
    "    ('9786170000103', 'Кайдашева сім''я', 5, 165.00, 6),\n"
    "    ('9786170000110', 'Нариси давньої історії', 8, 410.00, 2),\n"
    "    ('9786170000127', 'Козацька держава', 8, 295.00, 2),\n"
    "    ('9786170000134', 'Гетьмани', 7, 340.00, 3),\n"
    "    ('9786170000141', 'Довідник дат', 7, 120.00, 5);\n"
    '\n'
    'INSERT INTO reader (full_name, city) VALUES\n'
    "    ('Олена Шевченко', 'Київ'),\n"
    "    ('Іван Коваль', 'Львів'),\n"
    "    ('Марія Бондар', 'Київ'),\n"
    "    ('Петро Мельник', 'Харків'),\n"
    "    ('Софія Ткачук', 'Львів'),\n"
    "    ('Андрій Кравець', 'Київ'),\n"
    "    ('Наталія Лисенко', 'Харків'),\n"
    "    ('Дмитро Гончар', 'Львів'),\n"
    "    ('Юлія Пономаренко', 'Київ'),\n"
    "    ('Олег Савчук', 'Харків');\n"
    '\n'
    'INSERT INTO loan (reader_id, book_id, copies, loaned_on, returned_on) VALUES\n'
    "    (1, 1, 1, '2025-02-01', '2025-02-15'),\n"
    "    (1, 3, 1, '2025-03-01', '2025-03-20'),\n"
    "    (1, 10, 1, '2025-07-05', NULL),\n"
    "    (2, 6, 1, '2025-03-10', NULL),\n"
    "    (2, 1, 2, '2025-04-02', '2025-04-20'),\n"
    "    (3, 1, 1, '2025-03-15', '2025-04-01'),\n"
    "    (3, 8, 2, '2025-04-02', '2025-04-20'),\n"
    "    (3, 11, 1, '2025-05-10', '2025-05-30'),\n"
    "    (4, 3, 1, '2025-04-05', NULL),\n"
    "    (4, 10, 1, '2025-04-18', '2025-05-02'),\n"
    "    (5, 7, 1, '2025-05-01', '2025-05-12'),\n"
    "    (5, 11, 1, '2025-05-03', NULL),\n"
    "    (5, 13, 1, '2025-06-02', '2025-06-20'),\n"
    "    (6, 2, 1, '2025-05-20', NULL),\n"
    "    (6, 5, 1, '2025-06-01', '2025-06-15'),\n"
    "    (6, 8, 1, '2025-06-18', '2025-06-30'),\n"
    "    (7, 6, 2, '2025-06-10', NULL),\n"
    "    (7, 7, 1, '2025-06-12', '2025-06-28'),\n"
    "    (8, 5, 1, '2025-06-20', NULL),\n"
    "    (8, 8, 1, '2025-07-01', NULL),\n"
    "    (9, 13, 2, '2025-07-10', NULL),\n"
    "    (9, 1, 1, '2025-07-12', NULL);\n",
 2: '-- Схема набору 2: Магазин. PostgreSQL 18.\n'
    '-- Файл створює таблиці й наповнює їх початковими даними. Виконуйте його в ПОРОЖНІЙ схемі.\n'
    '\n'
    'CREATE TABLE category (\n'
    '    id        integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,\n'
    '    name      varchar(100) NOT NULL UNIQUE,\n'
    '    parent_id integer REFERENCES category (id)\n'
    ');\n'
    '\n'
    'CREATE TABLE product (\n'
    '    id      integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,\n'
    '    sku  varchar(20) NOT NULL UNIQUE,\n'
    '    title varchar(200) NOT NULL,\n'
    '    category_id   integer NOT NULL REFERENCES category (id),\n'
    '    price numeric(10,2) NOT NULL CHECK (price >= 0),\n'
    '    stock   integer NOT NULL DEFAULT 0 CHECK (stock >= 0)\n'
    ');\n'
    '\n'
    'CREATE TABLE customer (\n'
    '    id      integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,\n'
    '    full_name varchar(150) NOT NULL,\n'
    '    city varchar(60) NOT NULL\n'
    ');\n'
    '\n'
    'CREATE TABLE purchase (\n'
    '    id         integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,\n'
    '    customer_id integer NOT NULL REFERENCES customer (id),\n'
    '    product_id   integer NOT NULL REFERENCES product (id),\n'
    '    quantity    integer NOT NULL DEFAULT 1 CHECK (quantity > 0),\n'
    '    ordered_on   date NOT NULL,\n'
    '    shipped_on date\n'
    ');\n'
    '\n'
    '-- Початкові дані\n'
    '\n'
    'INSERT INTO category (name, parent_id) VALUES\n'
    "    ('Продукти', NULL),\n"
    "    ('Бакалія', 1),\n"
    "    ('Молочні вироби', 1),\n"
    "    ('Крупи', 2),\n"
    "    ('Макарони', 2),\n"
    "    ('Побутова хімія', NULL),\n"
    "    ('Прибирання', 6),\n"
    "    ('Для кухні', 7);\n"
    '\n'
    'INSERT INTO product (sku, title, category_id, price, stock) VALUES\n'
    "    ('SKU-0001', 'Молоко 2,5% 1 л', 3, 38.50, 40),\n"
    "    ('SKU-0002', 'Спагеті 500 г', 5, 42.90, 25),\n"
    "    ('SKU-0003', 'Гречка 1 кг', 4, 64.00, 30),\n"
    "    ('SKU-0004', 'Рис довгозернистий 1 кг', 4, 58.50, 0),\n"
    "    ('SKU-0005', 'Пенне 500 г', 5, 41.00, 18),\n"
    "    ('SKU-0006', 'Сир кисломолочний 350 г', 3, 72.00, 12),\n"
    "    ('SKU-0007', 'Вівсянка 800 г', 4, 36.80, 22),\n"
    "    ('SKU-0008', 'Пшоно 1 кг', 4, 33.00, 15),\n"
    "    ('SKU-0009', 'Фузилі 500 г', 5, 43.50, 9),\n"
    "    ('SKU-0010', 'Лазанья 500 г', 5, 55.00, 6),\n"
    "    ('SKU-0011', 'Засіб для посуду 500 мл', 8, 79.00, 14),\n"
    "    ('SKU-0012', 'Губки для посуду 5 шт', 8, 24.00, 50),\n"
    "    ('SKU-0013', 'Порошок пральний 3 кг', 7, 289.00, 8),\n"
    "    ('SKU-0014', 'Рідке мило 300 мл', 7, 47.00, 20);\n"
    '\n'
    'INSERT INTO customer (full_name, city) VALUES\n'
    "    ('Ольга Мазур', 'Київ'),\n"
    "    ('Богдан Кириленко', 'Одеса'),\n"
    "    ('Лариса Гнатюк', 'Київ'),\n"
    "    ('Роман Яковенко', 'Дніпро'),\n"
    "    ('Оксана Давиденко', 'Одеса'),\n"
    "    ('Максим Остапчук', 'Київ'),\n"
    "    ('Віра Шаповал', 'Дніпро'),\n"
    "    ('Артем Лозинський', 'Одеса'),\n"
    "    ('Галина Романюк', 'Київ'),\n"
    "    ('Станіслав Пилипенко', 'Дніпро');\n"
    '\n'
    'INSERT INTO purchase (customer_id, product_id, quantity, ordered_on, shipped_on) VALUES\n'
    "    (1, 1, 1, '2025-02-01', '2025-02-15'),\n"
    "    (1, 3, 1, '2025-03-01', '2025-03-20'),\n"
    "    (1, 10, 1, '2025-07-05', NULL),\n"
    "    (2, 6, 1, '2025-03-10', NULL),\n"
    "    (2, 1, 2, '2025-04-02', '2025-04-20'),\n"
    "    (3, 1, 1, '2025-03-15', '2025-04-01'),\n"
    "    (3, 8, 2, '2025-04-02', '2025-04-20'),\n"
    "    (3, 11, 1, '2025-05-10', '2025-05-30'),\n"
    "    (4, 3, 1, '2025-04-05', NULL),\n"
    "    (4, 10, 1, '2025-04-18', '2025-05-02'),\n"
    "    (5, 7, 1, '2025-05-01', '2025-05-12'),\n"
    "    (5, 11, 1, '2025-05-03', NULL),\n"
    "    (5, 13, 1, '2025-06-02', '2025-06-20'),\n"
    "    (6, 2, 1, '2025-05-20', NULL),\n"
    "    (6, 5, 1, '2025-06-01', '2025-06-15'),\n"
    "    (6, 8, 1, '2025-06-18', '2025-06-30'),\n"
    "    (7, 6, 2, '2025-06-10', NULL),\n"
    "    (7, 7, 1, '2025-06-12', '2025-06-28'),\n"
    "    (8, 5, 1, '2025-06-20', NULL),\n"
    "    (8, 8, 1, '2025-07-01', NULL),\n"
    "    (9, 13, 2, '2025-07-10', NULL),\n"
    "    (9, 1, 1, '2025-07-12', NULL);\n",
 3: '-- Схема набору 3: Облік обладнання. PostgreSQL 18.\n'
    '-- Файл створює таблиці й наповнює їх початковими даними. Виконуйте його в ПОРОЖНІЙ схемі.\n'
    '\n'
    'CREATE TABLE department (\n'
    '    id        integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,\n'
    '    name      varchar(100) NOT NULL UNIQUE,\n'
    '    parent_id integer REFERENCES department (id)\n'
    ');\n'
    '\n'
    'CREATE TABLE device (\n'
    '    id      integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,\n'
    '    inv_no  varchar(20) NOT NULL UNIQUE,\n'
    '    title varchar(200) NOT NULL,\n'
    '    department_id   integer NOT NULL REFERENCES department (id),\n'
    '    cost numeric(10,2) NOT NULL CHECK (cost >= 0),\n'
    '    quantity   integer NOT NULL DEFAULT 0 CHECK (quantity >= 0)\n'
    ');\n'
    '\n'
    'CREATE TABLE employee (\n'
    '    id      integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,\n'
    '    full_name varchar(150) NOT NULL,\n'
    '    building varchar(60) NOT NULL\n'
    ');\n'
    '\n'
    'CREATE TABLE issue (\n'
    '    id         integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,\n'
    '    employee_id integer NOT NULL REFERENCES employee (id),\n'
    '    device_id   integer NOT NULL REFERENCES device (id),\n'
    '    quantity    integer NOT NULL DEFAULT 1 CHECK (quantity > 0),\n'
    '    issued_on   date NOT NULL,\n'
    '    returned_on date\n'
    ');\n'
    '\n'
    '-- Початкові дані\n'
    '\n'
    'INSERT INTO department (name, parent_id) VALUES\n'
    "    ('Природничі науки', NULL),\n"
    "    ('Фізика', 1),\n"
    "    ('Біологія', 1),\n"
    "    ('Оптика', 2),\n"
    "    ('Електрика', 2),\n"
    "    ('Інформатика', NULL),\n"
    "    ('Мережі', 6),\n"
    "    ('Серверне обладнання', 7);\n"
    '\n'
    'INSERT INTO device (inv_no, title, department_id, cost, quantity) VALUES\n'
    "    ('INV-1001', 'Мікроскоп біологічний', 3, 18500.00, 4),\n"
    "    ('INV-1002', 'Мультиметр', 5, 1450.00, 10),\n"
    "    ('INV-1003', 'Оптичний стіл', 4, 24800.00, 1),\n"
    "    ('INV-1004', 'Набір лінз', 4, 3200.00, 6),\n"
    "    ('INV-1005', 'Осцилограф', 5, 15800.00, 2),\n"
    "    ('INV-1006', 'Центрифуга', 3, 21200.00, 1),\n"
    "    ('INV-1007', 'Спектроскоп', 4, 8700.00, 3),\n"
    "    ('INV-1008', 'Дифракційні ґратки', 4, 950.00, 12),\n"
    "    ('INV-1009', 'Блок живлення лабораторний', 5, 4300.00, 5),\n"
    "    ('INV-1010', 'Генератор сигналів', 5, 12600.00, 2),\n"
    "    ('INV-1011', 'Серверна шафа', 8, 32000.00, 1),\n"
    "    ('INV-1012', 'ДБЖ', 8, 9800.00, 3),\n"
    "    ('INV-1013', 'Комутатор 24 порти', 7, 11500.00, 4),\n"
    "    ('INV-1014', 'Маршрутизатор', 7, 6700.00, 3);\n"
    '\n'
    'INSERT INTO employee (full_name, building) VALUES\n'
    "    ('Василь Нагорний', 'Корпус А'),\n"
    "    ('Тетяна Руденко', 'Корпус Б'),\n"
    "    ('Ігор Савенко', 'Корпус А'),\n"
    "    ('Лідія Костенко', 'Корпус В'),\n"
    "    ('Павло Мороз', 'Корпус Б'),\n"
    "    ('Ірина Білик', 'Корпус А'),\n"
    "    ('Юрій Приходько', 'Корпус В'),\n"
    "    ('Алла Ткач', 'Корпус Б'),\n"
    "    ('Євген Литвин', 'Корпус А'),\n"
    "    ('Зоя Мартинюк', 'Корпус В');\n"
    '\n'
    'INSERT INTO issue (employee_id, device_id, quantity, issued_on, returned_on) VALUES\n'
    "    (1, 1, 1, '2025-02-01', '2025-02-15'),\n"
    "    (1, 3, 1, '2025-03-01', '2025-03-20'),\n"
    "    (1, 10, 1, '2025-07-05', NULL),\n"
    "    (2, 6, 1, '2025-03-10', NULL),\n"
    "    (2, 1, 2, '2025-04-02', '2025-04-20'),\n"
    "    (3, 1, 1, '2025-03-15', '2025-04-01'),\n"
    "    (3, 8, 2, '2025-04-02', '2025-04-20'),\n"
    "    (3, 11, 1, '2025-05-10', '2025-05-30'),\n"
    "    (4, 3, 1, '2025-04-05', NULL),\n"
    "    (4, 10, 1, '2025-04-18', '2025-05-02'),\n"
    "    (5, 7, 1, '2025-05-01', '2025-05-12'),\n"
    "    (5, 11, 1, '2025-05-03', NULL),\n"
    "    (5, 13, 1, '2025-06-02', '2025-06-20'),\n"
    "    (6, 2, 1, '2025-05-20', NULL),\n"
    "    (6, 5, 1, '2025-06-01', '2025-06-15'),\n"
    "    (6, 8, 1, '2025-06-18', '2025-06-30'),\n"
    "    (7, 6, 2, '2025-06-10', NULL),\n"
    "    (7, 7, 1, '2025-06-12', '2025-06-28'),\n"
    "    (8, 5, 1, '2025-06-20', NULL),\n"
    "    (8, 8, 1, '2025-07-01', NULL),\n"
    "    (9, 13, 2, '2025-07-10', NULL),\n"
    "    (9, 1, 1, '2025-07-12', NULL);\n"}
