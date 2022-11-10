import mysql.connector
import csv
import sys

maxInt=sys.maxsize

while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt=int(maxInt/10)


conn=mysql.connector.connect(host='localhost', user='root', password='Rathish@12', port='3306',database='bigdata')
cursor=conn.cursor()
#cursor.execute('CREATE DATABASE bigdata;')

create_table='CREATE TABLE president(Name_of_President longtext,Date_Of_Union_Address longtext,Link_to_Address longtext ,Filename_address longtext NOT NULL,Text_of_Address longtext NOT NULL)'
cursor.execute(create_table)
print("Table created")

with open ('big_data.csv','r') as f:
    reader=csv.reader(f)
    insert_data=("INSERT INTO president(Name_of_President,Date_Of_Union_Address,Link_to_Address,Filename_address,Text_of_Address)"
           "VALUES (%s,%s,%s,%s,%s)")
    for data in reader:
       cursor.execute(insert_data,data)
       conn.commit()
       
    
         
cursor.close()
conn.close()
print("Data base created and data uploaded successfully")

