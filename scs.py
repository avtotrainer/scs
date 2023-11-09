import sqlite3

class SchoolDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def create_schools_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS schools
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             name TEXT NOT NULL,
                             address TEXT NOT NULL,
                             phone TEXT NOT NULL,
                             inn INTEGER(9) NOT NULL UNIQUE,
                             code INTEGER(4) NOT NULL UNIQUE)''')

    def create_personnel_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS personnel
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             name TEXT NOT NULL,
                             role TEXT NOT NULL,
                             school_id INTEGER,
                             FOREIGN KEY (school_id) REFERENCES schools(id))''')

    def create_personnel_schools_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS personnel_schools
                             (personnel_id INTEGER,
                             school_id INTEGER,
                             FOREIGN KEY (personnel_id) REFERENCES personnel(id),
                             FOREIGN KEY (school_id) REFERENCES schools(id))''')

    def create_classes_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS classes
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             grade INTEGER NOT NULL,
                             parallel TEXT NOT NULL,
                             school_id INTEGER,
                             FOREIGN KEY (school_id) REFERENCES schools(id))''')

    def create_students_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             name TEXT NOT NULL,
                             class_id INTEGER,
                             FOREIGN KEY (class_id) REFERENCES classes(id))''')

    def create_departments_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS departments
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             name TEXT NOT NULL)''')

    def create_subjects_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS subjects
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             name TEXT NOT NULL,
                             department_id INTEGER,
                             FOREIGN KEY (department_id) REFERENCES departments(id))''')

    def create_teacher_subjects_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS teacher_subjects
                             (teacher_id INTEGER,
                             subject_id INTEGER,
                             FOREIGN KEY (teacher_id) REFERENCES personnel(id),
                             FOREIGN KEY (subject_id) REFERENCES subjects(id))''')

    def insert_school(self, name, address, phone, inn, code):
        self.cursor.execute("INSERT INTO schools (name, address, phone, inn, code) VALUES (?, ?, ?, ?, ?)",
                            (name, address, phone, inn, code))

    def insert_personnel(self, name, role, school_id):
        self.cursor.execute("INSERT INTO personnel (name, role, school_id) VALUES (?, ?, ?)",
                            (name, role, school_id))

    def insert_personnel_schools(self, personnel_id, school_id):
        self.cursor.execute("INSERT INTO personnel_schools (personnel_id, school_id) VALUES (?, ?)",
                            (personnel_id, school_id))

    def insert_class(self, grade, parallel, school_id):
        self.cursor.execute("INSERT INTO classes (grade, parallel, school_id) VALUES (?, ?, ?)",
                            (grade, parallel, school_id))

    def insert_student(self, name, class_id):
        self.cursor.execute("INSERT INTO students (name, class_id) VALUES (?, ?)",
                            (name, class_id))

    def insert_department(self, name):
        self.cursor.execute("INSERT INTO departments (name) VALUES (?)",
                            (name,))

    def insert_subject(self, name, department_id):
        self.cursor.execute("INSERT INTO subjects (name, department_id) VALUES (?, ?)",
                            (name, department_id))

    def insert_teacher_subject(self, teacher_id, subject_id):
        self.cursor.execute("INSERT INTO teacher_subjects (teacher_id, subject_id) VALUES (?, ?)",
                            (teacher_id, subject_id))

    def commit_changes(self):
        self.conn.commit()


# Пример использования класса SchoolDatabase для создания таблиц и добавления данных

# Создание экземпляра класса SchoolDatabase
db = SchoolDatabase('scs.db')

# Подключение к базе данных
db.connect()

# Создание таблицы для учебных заведений
db.create_schools_table()

# Пример добавления данных в таблицу учебных заведений
db.insert_school('Школа №1', 'ул. Центральная, 123', '123-456-789', 123456789, 1234)
db.insert_school('Школа №2', 'ул. Парковая, 456', '987-654-321', 987654321, 5678)

# Создание таблицы для персонала
db.create_personnel_table()

# Пример добавления данных в таблицу персонала
db.insert_personnel('Иванов Иван', 'Учитель', 1)
db.insert_personnel('Петров Петр', 'Учитель', 1)
db.insert_personnel('Сидорова Анна', 'Администратор', 1)

# Создание таблицы для связи между персоналом и школами
db.create_personnel_schools_table()

# Пример добавления связей между персоналом и школами
db.insert_personnel_schools(1, 1)
db.insert_personnel_schools(2, 1)
db.insert_personnel_schools(3, 1)

# Создание таблицы для классов
db.create_classes_table()

# Пример добавления данных в таблицу классов
db.insert_class(1, 'А', 1)
db.insert_class(1, 'Б', 1)
db.insert_class(2, 'А', 1)

# Создание таблицы для учеников
db.create_students_table()

# Пример добавления данных в таблицу учеников
db.insert_student('Иванов Иван', 1)
db.insert_student('Петров Петр', 2)

# Создание таблицы для кафедр
db.create_departments_table()

# Пример добавления данных в таблицу кафедр
db.insert_department('Математика')
db.insert_department('История')

# Создание таблицы для предметов
db.create_subjects_table()

# Пример добавления данных в таблицу предметов
db.insert_subject('Алгебра', 1)
db.insert_subject('Геометрия', 1)

# Создание таблицы для связи между учителями и предметами
db.create_teacher_subjects_table()

# Пример добавления связей между учителями и предметами
db.insert_teacher_subject(1, 1)
db.insert_teacher_subject(1, 2)

# Сохранение изменений
db.commit_changes()

# Отключение от базы данных
db.disconnect()