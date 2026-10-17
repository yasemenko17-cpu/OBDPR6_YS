-- Схема набору 3: Облік обладнання. PostgreSQL 18.
-- Файл створює таблиці й наповнює їх початковими даними. Виконуйте його в ПОРОЖНІЙ схемі.

CREATE TABLE department (
    id        integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name      varchar(100) NOT NULL UNIQUE,
    parent_id integer REFERENCES department (id)
);

CREATE TABLE device (
    id      integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    inv_no  varchar(20) NOT NULL UNIQUE,
    title varchar(200) NOT NULL,
    department_id   integer NOT NULL REFERENCES department (id),
    cost numeric(10,2) NOT NULL CHECK (cost >= 0),
    quantity   integer NOT NULL DEFAULT 0 CHECK (quantity >= 0)
);

CREATE TABLE employee (
    id      integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name varchar(150) NOT NULL,
    building varchar(60) NOT NULL
);

CREATE TABLE issue (
    id         integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    employee_id integer NOT NULL REFERENCES employee (id),
    device_id   integer NOT NULL REFERENCES device (id),
    quantity    integer NOT NULL DEFAULT 1 CHECK (quantity > 0),
    issued_on   date NOT NULL,
    returned_on date
);

-- Початкові дані

INSERT INTO department (name, parent_id) VALUES
    ('Природничі науки', NULL),
    ('Фізика', 1),
    ('Біологія', 1),
    ('Оптика', 2),
    ('Електрика', 2),
    ('Інформатика', NULL),
    ('Мережі', 6),
    ('Серверне обладнання', 7);

INSERT INTO device (inv_no, title, department_id, cost, quantity) VALUES
    ('INV-1001', 'Мікроскоп біологічний', 3, 18500.00, 4),
    ('INV-1002', 'Мультиметр', 5, 1450.00, 10),
    ('INV-1003', 'Оптичний стіл', 4, 24800.00, 1),
    ('INV-1004', 'Набір лінз', 4, 3200.00, 6),
    ('INV-1005', 'Осцилограф', 5, 15800.00, 2),
    ('INV-1006', 'Центрифуга', 3, 21200.00, 1),
    ('INV-1007', 'Спектроскоп', 4, 8700.00, 3),
    ('INV-1008', 'Дифракційні ґратки', 4, 950.00, 12),
    ('INV-1009', 'Блок живлення лабораторний', 5, 4300.00, 5),
    ('INV-1010', 'Генератор сигналів', 5, 12600.00, 2),
    ('INV-1011', 'Серверна шафа', 8, 32000.00, 1),
    ('INV-1012', 'ДБЖ', 8, 9800.00, 3),
    ('INV-1013', 'Комутатор 24 порти', 7, 11500.00, 4),
    ('INV-1014', 'Маршрутизатор', 7, 6700.00, 3);

INSERT INTO employee (full_name, building) VALUES
    ('Василь Нагорний', 'Корпус А'),
    ('Тетяна Руденко', 'Корпус Б'),
    ('Ігор Савенко', 'Корпус А'),
    ('Лідія Костенко', 'Корпус В'),
    ('Павло Мороз', 'Корпус Б'),
    ('Ірина Білик', 'Корпус А'),
    ('Юрій Приходько', 'Корпус В'),
    ('Алла Ткач', 'Корпус Б'),
    ('Євген Литвин', 'Корпус А'),
    ('Зоя Мартинюк', 'Корпус В');

INSERT INTO issue (employee_id, device_id, quantity, issued_on, returned_on) VALUES
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
