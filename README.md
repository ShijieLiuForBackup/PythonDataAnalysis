# PythonDataAnalysis

This project uses data from two excel files to
do a behavioural analysis for restaurants in an 
area. 

Food Violation 
This assignment has 4 python files,1 database
file, 1 excel file of ViolationTypes and 1
directory has the 2 original excel files
(inspections, and violations).

db_create.py file 
defined the database creatation
it has two table queries, and codes for inserting
data from excel to databaseA2.db(the database
created for this assignment).

sql_food.py file 
lists the distinctive business 
that have at least 1 violation.Also a count number
of business with their name and violation numbers.

excel_food.py file 
solved the task 2, created 
another table of ViolationTypes.excel, and 
also insert data from query depends on assignment
requirement--violation code and its description, 
also provides the happend count times and total 
times. 

numpy_food.py file 
shows the plot pictures of data,
using queies to retrieve data from database and using
sqlite cursor to execute each queries. 
It has a function named collecte_output() to execute
each query and return the number of violations for 
each month. 

The numpy_food.py file 
runs at the Spyder IDE may take
a longer time to execute the output, Please 
give it some more mins to output the data.
For each question, I comment the question number and
each line should see the description for each line's
purpose.

