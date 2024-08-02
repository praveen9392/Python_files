import sqlite3
conn=sqlite3.connect(r"c:/python/database.db")  # creating the connection
cursor=conn.cursor()     # creating cursor object is to execute sql commands in the database
cursor.execute()         # if require insert the data 
cursor.commit()          #save the transaction
rows=cursor.fetchall()
for row in rows:
    print(row)

cursor.close()      # after executing all the query's ,need to save and close the cursor object
conn.close()        #must and should close the connection if not ,when you working with other modules that may link with database at the time may get database error already opening in some where ,did not close the connection


