import chortombaev_arsen_hw_8 as db_main
import sqlite3


db_main.city_print('chortombaev.db')
while True:
    breaker = int(input('Хотите ли вы продолжить? Напишите 0 если нет, а если да то 1: '))
    if breaker == 0:
        break
    elif breaker == 1:
        pass
    add = db_main.find_sudent('chortombaev.db', int(input('''Вы можете отобразить список учеников по выбрынному ID
города из перечня городов выще: ''')))

