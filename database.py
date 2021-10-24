#import modules

from enum import unique
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

#insert query for login
insert_sql_login='''
insert into public."login"("userId","userN","passW") values(1,'Rahul','2015')
'''

#insert query for registration
insert_sql_registration='''
insert into public."Registrations"("userId","userN","passW","emailId") values('1','Rahul','2015','1707214@kiit.ac.in')
'''

#insert query for searchengine
insert_sql_query='''
insert into public."Searchengine"("iD","fileN","fileL") values(7,'A','heypy')
'''

#execution
hostman=connection.cursor()
hostman.execute(insert_sql_query)
hostman.execute(insert_sql_login)
hostman.execute(insert_sql_registration)
connection.commit()
print("record is created")
connection.close()





















