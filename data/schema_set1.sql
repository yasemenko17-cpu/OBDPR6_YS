-- Схема набору 1: Бібліотека. PostgreSQL 18.
-- Файл створює таблиці й наповнює їх початковими даними. Виконуйте його в ПОРОЖНІЙ схемі.

CREATE TABLE genre (
    id        integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name      varchar(100) NOT NULL UNIQUE,
    parent_id integer REFERENCES genre (id)
);

CREATE TABLE book (
    id      integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    isbn  varchar(20) NOT NULL UNIQUE,
    title varchar(200) NOT NULL,
    genre_id   integer NOT NULL REFERENCES genre (id),
    price numeric(10,2) NOT NULL CHECK (price >= 0),
    copies   integer NOT NULL DEFAULT 0 CHECK (copies >= 0)
);

CREATE TABLE reader (
    id      integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name varchar(150) NOT NULL,
    city varchar(60) NOT NULL
);

CREATE TABLE loan (
    id         integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    reader_id integer NOT NULL REFERENCES reader (id),
    book_id   integer NOT NULL REFERENCES book (id),
    copies    integer NOT NULL DEFAULT 1 CHECK (copies > 0),
    loaned_on   date NOT NULL,
    returned_on date
);

-- Початкові дані

INSERT INTO genre (name, parent_id) VALUES
    ('Художня література', NULL),
    ('Проза', 1),
    ('Поезія', 1),
    ('Роман', 2),
    ('Повість', 2),
    ('Наукова література', NULL),
    ('Історія', 6),
    ('Історія України', 7);

INSERT INTO book (isbn, title, genre_id, price, copies) VALUES
    ('9786170000011', 'Кобзар', 3, 320.00, 5),
    ('9786170000028', 'Тіні забутих предків', 5, 210.50, 0),
    ('9786170000035', 'Захар Беркут', 4, 185.00, 3),
    ('9786170000042', 'Місто', 4, 260.00, 0),
    ('9786170000059', 'Intermezzo', 5, 150.00, 2),
    ('9786170000066', 'Лісова пісня', 3, 175.75, 7),
    ('9786170000073', 'Тигролови', 4, 230.00, 1),
    ('9786170000080', 'Маруся', 4, 140.00, 4),
    ('9786170000097', 'Fata Morgana', 5, 199.90, 1),
    ('9786170000103', 'Кайдашева сім''я', 5, 165.00, 6),
    ('9786170000110', 'Нариси давньої історії', 8, 410.00, 2),
    ('9786170000127', 'Козацька держава', 8, 295.00, 2),
    ('9786170000134', 'Гетьмани', 7, 340.00, 3),
    ('9786170000141', 'Довідник дат', 7, 120.00, 5);

INSERT INTO reader (full_name, city) VALUES
    ('Олена Шевченко', 'Київ'),
    ('Іван Коваль', 'Львів'),
    ('Марія Бондар', 'Київ'),
    ('Петро Мельник', 'Харків'),
    ('Софія Ткачук', 'Львів'),
    ('Андрій Кравець', 'Київ'),
    ('Наталія Лисенко', 'Харків'),
    ('Дмитро Гончар', 'Львів'),
    ('Юлія Пономаренко', 'Київ'),
    ('Олег Савчук', 'Харків');

INSERT INTO loan (reader_id, book_id, copies, loaned_on, returned_on) VALUES
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
