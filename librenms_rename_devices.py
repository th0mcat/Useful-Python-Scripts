import mysql.connector
import csv

# Specify the database user and server information
mydb = mysql.connector.connect(
  host=$MYSQL_IP,
  user=$MYSQL_USER,
  password=$MYSQL_PASS,
  database=$MYSQL_DB
)

mycursor = mydb.cursor()

# Open a CSV file that contains two columns, old_hostname and new_hostname.   
with open('librenms_fix.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        old_hostname = str(row[0])
        new_hostname = str(row[1])
        sql = str("UPDATE devices SET hostname = '" + new_hostname + "' WHERE hostname = '" + old_hostname + "'")
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
