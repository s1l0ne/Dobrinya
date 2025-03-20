import psycopg2


def connect():
    return psycopg2.connect(
        dbname='RGD',
        user='postgres',
        password='1112111',
        host='localhost',
        port='5432'
    )
