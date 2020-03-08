# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:57:44 2020

@author: liush
"""

#产生随即数据， 并把随即数据存入Excel文件

import os.path
import xlwt
from faker import Faker
import random

fak = Faker()

#create a new excel file for storing data needed
if(os.path.exists('student2.xlsx') == False):
    #wb = openpyxl.Workbook()
    wb = xlwt.Workbook()
    #sheet = wb.active
    sheet = wb.add_sheet('student2 sheet', cell_overwrite_ok=True)
    #wb.save('frankBook.xlsx')
    col1=sheet.col(0)
else:
    print('the file already exists')
    
#set column
#初始化第一行
row0 = [u'student_id',u'student_name',u'gender']
for i in range(0, len(row0)):
    sheet.write(0, i , row0[i])

#set first column data
#设置初始化第一列数据    
col1_data = []
for j in range(11001, 50001):
    col1_data = [fak.ssn()]
    sheet.write(j-11000,0, j+1)
    
#第二列数据
col2_data = []
for k in range(11001,50001):
    col2_data = [fak.name()]
    sheet.write(k-11000, 1, col2_data)
    
#第3列数据
col3_data = []
for k in range(11001,50001):
    col3_data = [str(random.randint(0,1))]
    sheet.write(k-11000, 2, col3_data)


    
wb.save('student2.xls')