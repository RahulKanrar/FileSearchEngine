#import modules
import psycopg2
import logging

#database connection
connection= psycopg2.connect(
    database= "searchengine",
    user="postgres",
    password="RAHULJACK67",
    host="localhost",
    port="5432")
# print(connection)

#delete record query for searchengine
delete_sql_query='''
DELETE FROM public."Searchengine"
WHERE "iD"=2;
'''

#delete record query for registration
delete_sql_registration='''
DELETE FROM public."Registrations"
WHERE "userId"=2;
'''

#delete record query for login
delete_sql_login='''
DELETE FROM public."login"
WHERE "userId"=2;
'''

hostman=connection.cursor()
hostman.execute(delete_sql_query)
hostman.execute(delete_sql_query)
hostman.execute(delete_sql_query)
connection.commit()
print("record is deleted")
connection.close()