import sqlite3


def city_print(db_file):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT id, title FROM cities'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)


def find_sudent(db_file, city_id):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT s.*,
       c.title, c.area, co.title
  FROM students AS s
       INNER JOIN
       cities AS c ON s.cities_id = c.id
       INNER JOIN
       countries AS co ON c.country_id = co.id
       WHERE c.id = ?;
'''
            cursor = connection.cursor()
            cursor.execute(sql, (city_id,))
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)


db_filename = 'chortombaev.db'
# city_print(db_filename)
# find_sudent(db_filename, city_id=5)