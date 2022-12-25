import csv
import view

def write_date(str_date):
        with open('db.csv', 'a',newline= '',encoding= 'utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(str_date)