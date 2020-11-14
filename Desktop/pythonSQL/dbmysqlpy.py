import mysql.connector


try:
    cnx = mysql.connector.connect(user='root',password='password',host='127.0.0.1',database='nicksdb')
    cursor = cnx.cursor()
    cursor.execute("use nicksdb;")
    
    cursor.execute('SELECT * FROM employees;')
    print cursor.fetchall()
    cnx.commit();

except Exception as e:
    print('error on ' + e)

finally:
    cnx.close()
