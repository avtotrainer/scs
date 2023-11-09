import sqlite3

# Создание базы данных и подключение к ней
conn = sqlite3.connect('scs.db')
c = conn.cursor()

# Создание таблицы для учебных заведений с уникальными идентификаторами
c.execute('''CREATE TABLE IF NOT EXISTS schools
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             address TEXT NOT NULL,
             phone TEXT NOT NULL,
             inn INTEGER(9) NOT NULL UNIQUE,
             code INTEGER(4) NOT NULL UNIQUE)''')

# Пример добавления данных в таблицу с уникальными идентификаторами
c.execute("INSERT INTO schools (name, address, phone, inn, code) VALUES ('Школа №1', 'ул. Центральная, 123', '123-456-789', 123456789, 1234)")
c.execute("INSERT INTO schools (name, address, phone, inn, code) VALUES ('Школа №2', 'ул. Парковая, 456', '987-654-321', 987654321, 5678)")



# Создание таблицы для персонала
c.execute('''CREATE TABLE IF NOT EXISTS personnel
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             role TEXT NOT NULL,
             school_id INTEGER,
             FOREIGN KEY (school_id) REFERENCES schools(id))''')

# Пример добавления данных в таблицу персонала
c.execute("INSERT INTO personnel (name, role, school_id) VALUES ('Иванов Иван', 'Учитель', 1)")
c.execute("INSERT INTO personnel (name, role, school_id) VALUES ('Петров Петр', 'Учитель', 1)")
c.execute("INSERT INTO personnel (name, role, school_id) VALUES ('Сидорова Анна', 'Администратор', 1)")
c.execute("INSERT INTO personnel (name, role, school_id) VALUES ('Смирнова Елена', 'Сотрудник столовой', 1)")
c.execute("INSERT INTO personnel (name, role, school_id) VALUES ('Козлов Василий', 'Директор', 1)")



# Создание таблицы для персонала
c.execute('''CREATE TABLE IF NOT EXISTS personnel
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             role TEXT NOT NULL)''')

# Создание таблицы для связи между персоналом и школами
c.execute('''CREATE TABLE IF NOT EXISTS personnel_schools
             (personnel_id INTEGER,
             school_id INTEGER,
             FOREIGN KEY (personnel_id) REFERENCES personnel(id),
             FOREIGN KEY (school_id) REFERENCES schools(id))''')

# Пример добавления данных в таблицу персонала
c.execute("INSERT INTO personnel (name, role) VALUES ('Иванов Иван', 'Учитель')")
c.execute("INSERT INTO personnel (name, role) VALUES ('Петров Петр', 'Учитель')")
c.execute("INSERT INTO personnel (name, role) VALUES ('Сидорова Анна', 'Администратор')")
c.execute("INSERT INTO personnel (name, role) VALUES ('Смирнова Елена', 'Сотрудник столовой')")
c.execute("INSERT INTO personnel (name, role) VALUES ('Козлов Василий', 'Директор')")

# Пример добавления связей между персоналом и школами
c.execute("INSERT INTO personnel_schools (personnel_id, school_id) VALUES (1, 1)")
c.execute("INSERT INTO personnel_schools (personnel_id, school_id) VALUES (2, 1)")
c.execute("INSERT INTO personnel_schools (personnel_id, school_id) VALUES (3, 1)")
c.execute("INSERT INTO personnel_schools (personnel_id, school_id) VALUES (4, 1)")
c.execute("INSERT INTO personnel_schools (personnel_id, school_id) VALUES (5, 1)")
c.execute("INSERT INTO personnel_schools (personnel_id, school_id) VALUES (1, 2)")
c.execute("INSERT INTO personnel_schools (personnel_id, school_id) VALUES (3, 2)")



# Создание таблицы для классов
c.execute('''CREATE TABLE IF NOT EXISTS classes
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             grade INTEGER NOT NULL,
             parallel TEXT NOT NULL,
             school_id INTEGER,
             FOREIGN KEY (school_id) REFERENCES schools(id))''')

# Пример добавления данных в таблицу классов
c.execute("INSERT INTO classes (grade, parallel, school_id) VALUES (1, 'А', 1)")
c.execute("INSERT INTO classes (grade, parallel, school_id) VALUES (1, 'Б', 1)")
c.execute("INSERT INTO classes (grade, parallel, school_id) VALUES (2, 'А', 1)")
c.execute("INSERT INTO classes (grade, parallel, school_id) VALUES (2, 'Б', 1)")
c.execute("INSERT INTO classes (grade, parallel, school_id) VALUES (1, 'А', 2)")
c.execute("INSERT INTO classes (grade, parallel, school_id) VALUES (1, 'Б', 2)")

# Сохранение изменений и закрытие соединения

# Создание таблицы для детей
c.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             class_id INTEGER,
             FOREIGN KEY (class_id) REFERENCES classes(id))''')

# Пример добавления данных в таблицу детей
c.execute("INSERT INTO students (name, class_id) VALUES ('Иванов Иван', 1)")
c.execute("INSERT INTO students (name, class_id) VALUES ('Петров Петр', 2)")
c.execute("INSERT INTO students (name, class_id) VALUES ('Сидорова Анна', 1)")
c.execute("INSERT INTO students (name, class_id) VALUES ('Смирнова Елена', 2)")

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()