from django.db import connection


class MyConn:

    def connect(type, columns, dataType, table):

        query = MyConn.query(type, columns, dataType, table)
        print(query)
        cursor = connection.cursor()
        cursor.execute(query)
        #rows = cursor.fetchall()

        return cursor.fetchall()

    def query(type, columns, dataType, table):
        query = ''

        if type == 'select':
            query = MyConn.select(columns, table)
        elif type == 'create':
            query = MyConn.create(columns, dataType, table)

        return query

    def select(columns, table):
        query = 'select'

        for column in columns:
            query = query + ' ' + column + ','

        query = query[:-1]

        query = query + ' from ' + table

        return query

    def create(columns, dataType, table):
        query = 'create table ' + table + ' ('

        for name, type in columns.items():
            query = query + ' ' + name + ' ' + type + ','

        query = query[:-1]

        query = ')'

        return query
