'''
Created on Mar 27, 2016

@author: edward
'''
import psycopg2
import ppygis

if __name__ == '__main__':
    # Connect to an existing spatial database
    connection = psycopg2.connect(database = 'geodjango', user = 'postgres', password='dapeng', host='localhost',port='5432')
    print connection
    cursor = connection.cursor()
    # Create a table with a geometry column
    cursor.execute('CREATE TABLE test(geometry GEOMETRY)')
    # Insert a point into the table
    cursor.execute('INSERT INTO test VALUES(%s)', (ppygis.Point(1.0, 2.0),))
    # Retrieve the point from the table and print it
    cursor.execute('SELECT * FROM test')
    point = cursor.fetchone()[0]
    print point
    # Modify the point and print it

    
    # Disconnect from the database
    connection.commit()
    cursor.close()
    connection.close()
    pass