import sqlite3


# connect to the database
connection = sqlite3.connect('databaseA2.db')
cursor = connection.cursor();


#create previous violations table
sql_command_previous_violations = """create table if not exists previousviolations(
id integer primary key, facility_name varchar(40), facility_address varchar(30),
facility_zip varchar(10), facility_city varchar(20));""" 
cursor.execute(sql_command_previous_violations)


#check if the table is empty
check_table_empty = cursor.execute('select count(*) from previousviolations').fetchall()
check_table_empty = check_table_empty[0][0]

if(check_table_empty == 0):
    # the select query 
    select_distinct_query = "select distinct inspections.facility_name, inspections.facility_address, inspections.facility_zip,\
    inspections.facility_city from inspections  join violations on inspections.serial_number = violations.serial_number \
    order by facility_name"
    
    #get all result of distinct
    distinct_result = cursor.execute(select_distinct_query).fetchall()
    
    result_rows = len(distinct_result)
    #insert data to the previousviolations table
    for row in range(0, result_rows):
        cursor.execute('INSERT INTO previousviolations VALUES (NULL, ?, ?, ?, ?)',
                       (distinct_result[row][0], distinct_result[row][1], distinct_result[row][2], distinct_result[row][3]))


violation_times = cursor.execute('select inspections.facility_name, count(inspections.facility_name) as vio_count from inspections\
                                 join violations on inspections.serial_number = violations.serial_number group by  facility_name\
                                 order by vio_count').fetchall()

max_row = len(violation_times)

for row in range(0, max_row):
    print(violation_times[row][0], violation_times[row][1])
    

connection.commit()
print('done')
connection.close()