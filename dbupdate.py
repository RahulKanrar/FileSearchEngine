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

#update record query for login
update_sql_login='''
update public."login" set "userN" = 'Rup',"passW"= '2016' where "iD"=1;
'''

#update record query for registration
update_sql_registration='''
update public."Registrations" set "userN" = 'Rup',"passW"= '1788' , "emailId"='rahulkanrar450@gmail.com' where "iD"=3;
'''

#update record query for searchengine
update_sql_query='''
update public."Searchengine" set "fileN" = 'abc',"fileL"= 'def' where "iD"=2;
'''

hostman=connection.cursor()
try:
    hostman.execute(insert_sql_query)
    hostman.execute(insert_sql_registration)
    hostman.execute(insert_sql_login)
    connection.commit()
    print("record is updated")
except Exception as Argument:
    logging.error("record is not updated")
finally:
    connection.close()