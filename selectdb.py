import psycopg2
import logging

connection= psycopg2.connect(
    database= "SEARCHENGINE",
    user="postgres",
    password="1705",
    host="localhost",
    port="5432")
# print(connection)
##selecting records
table_select_registration='''
     select * from Registration
'''

table_select_login='''
     select * from Login
'''

table_select_query='''
     select * from 
'''

hostman= connection.cursor()
hostman.execute(table_select_query)
print("\nQUERY TABLE")
rows1=hostman.fetchall()
for each_row in rows1:
    print(each_row)
print("\nREGISTRATION TABLE")
hostman.execute(table_select_registration)
rows2=hostman.fetchall()
for each_row in rows2:
    print(each_row)
print("\nLOGIN TABLE")
hostman.execute(table_select_login)
rows3=hostman.fetchall()
for each_row in rows3:
    print(each_row)