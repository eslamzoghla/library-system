import sqlite3

DB_Name = "Books.db"

# Function to add book to database
def add_book(book_name, author, category, book_version, release_date, pages, copy, book_shelf, note):
    conn = sqlite3.connect(DB_Name)
    conn.execute(
        '''insert into bookinfo( book_name, author, category, book_version, release_date, pages, copy, book_shelf, note) values(?,?,?,?,?,?,?,?,?)''',
        (book_name, author, category, book_version, release_date, pages, copy, book_shelf, note))
    conn.commit()
    conn.close()


# Function to update record in database
def update_book(book_name, author, category, book_version, release_date, pages, copy, book_shelf):
    conn = sqlite3.connect(DB_Name)
    conn.execute(
        '''update bookinfo set  author=?, category=?, book_version=?, release_date=?, pages=?, copy=?, book_shelf=? where 
        book_name=?''',
        (author, category, book_version, release_date, pages, copy, book_shelf, book_name))
    conn.commit()
    conn.close()


# Function to delete record from database
def delete_book(book_name):
    conn = sqlite3.connect(DB_Name)
    conn.execute('''delete from bookinfo where book_name=?''', [book_name])
    conn.commit()
    conn.close()


# Function to get record with id
def search_book_data(book_name):
    conn = sqlite3.connect(DB_Name)
    cursor = conn.execute('''select * from bookinfo where book_name=? ''', [book_name])
    data = list(cursor)
    print(data)
    conn.close()
    return data


# Function to get all records in database
def get_book_data():
    conn = sqlite3.connect(DB_Name)
    cursor = conn.execute('''select * from bookinfo''')
    data = list(cursor)
    conn.close()
    return data


# Function to add data to Student database
def add_student(stu_id, stu_name, academic_year, phone, return_date, today_date, book_name):
    conn = sqlite3.connect(DB_Name)
    conn.execute(
        '''insert into studentinfo(stu_id, stu_name, academic_year, phone, return_date, today_date, book_name) values(?, ?, ?, ?, ?, ?, ?)''',
        (stu_id, stu_name, academic_year, phone, return_date, today_date, book_name))
    conn.commit()
    conn.close()


# Function to delete record from database
def delete_student(stu_id):
    conn = sqlite3.connect(DB_Name)
    conn.execute('''delete from studentinfo where stu_id=?''', [stu_id])
    conn.commit()
    conn.close()


# Function to update record to database
def updata_student(stu_id, stu_name, academic_year, phone, book_name):
    conn = sqlite3.connect(DB_Name)
    conn.execute('''update studentinfo set stu_name=?, academic_year=?, phone=?, book_name=? where stu_id=?''',
                 (stu_name, academic_year, phone, book_name, stu_id))
    conn.commit()
    conn.close()


# Function to get all records in database
def get_student_data():
    conn = sqlite3.connect(DB_Name)
    cursor = conn.execute('''select * from studentinfo''')
    data = list(cursor.fetchall())
    conn.close()
    return data


# Function to get a record with id in database
def search_student_data(stu_id):
    conn = sqlite3.connect(DB_Name)
    cursor = conn.execute('''select * from studentinfo where stu_id=?''', [stu_id])
    data = list(cursor.fetchall())
    conn.close()
    return data


def get_return_date(id):
    conn = sqlite3.connect(DB_Name)
    cursor = conn.execute('''select return_date from studentinfo where stu_id=? ''', [id])
    data = list(cursor)
    conn.close()
    return data
