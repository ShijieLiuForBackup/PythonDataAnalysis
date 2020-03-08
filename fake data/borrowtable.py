# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 17:16:06 2020

@author: liush
"""

import os.path
import xlwt
from faker import Faker

fak = Faker()

#create a new excel file for storing data needed
if(os.path.exists('borrowtable.xlsx') == False):
    #wb = openpyxl.Workbook()
    wb = xlwt.Workbook()
    #sheet = wb.active
    sheet = wb.add_sheet('borrowtable sheet', cell_overwrite_ok=True)
    #wb.save('frankBook.xlsx')
    col1=sheet.col(0)
else:
    print('the file already exists')
    
#set column
#初始化第一行
row0 = [u'book_id',u'student_id',u'borrow_time',u'back_time']
for i in range(0, len(row0)):
    sheet.write(0, i , row0[i])

#set first column data
#设置初始化第一列数据    
col1_data = []
for j in range(11000):
    col1_data = [fak.ssn()]
    sheet.write(j+1,0, j+1)
    
#第二列数据
col2_data = []
for k in range(11000):
    col2_data = [fak.ssn()]
    sheet.write(k+1, 1, k+1)
    
#第3列数据
col3_data = []
for k in range(11000):
    col3_data = [fak.date(pattern="%Y-%m-%d", end_datetime=None)]
    sheet.write(k+1, 2, col3_data)

#第四列数据
col4_data = []
for k in range(11000):
    col4_data = [fak.date(pattern="%Y-%m-%d", end_datetime=None)]
    sheet.write(k+1, 3, col4_data)

    
wb.save('borrowtable.xls')