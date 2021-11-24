#Vaghasiya Sahll H.
#1901EE65

import os
from openpyxl import load_workbook
import pandas as pd


df1 = pd.read_csv('course_registered_by_all_students.csv')
print(len(df1))

df = pd.read_csv('course_feedback_submitted_by_students.csv')
df = df.set_index('stud_roll')

df2 = pd.read_csv('course_master_dont_open_in_excel.csv')
df2 = df2.set_index('subno')

df3 = pd.read_csv('studentinfo.csv')
df3 = df3.set_index('Roll No')

list = []

for row in range(len(df1)):
	
    roll = df1.loc[row, 'rollno'] 
    sub = df1.loc[row, 'subno']
    ltp = df2.loc[sub, 'ltp']
	
    schedule = df1.loc[row, 'schedule_sem'] 
	
    try:
        name = df3.loc[roll, 'Name']
    except:
        name = "NA_IN_STUDENTINFO"
    register = df1.loc[row, 'register_sem']
	
    
    try:
        email = df3.loc[roll, 'email']
    except:
        email = "NA_IN_STUDENTINFO"
    try:
        aemail = df3.loc[roll, 'aemail']
    except:
        aemail = "NA_IN_STUDENTINFO"
    try:
        contact = df3.loc[roll, 'contact']
    except:
        contact = "NA_IN_STUDENTINFO"
	

    count1 = 0
	
    if ltp[0] != '0':
        count1 += 1
    if ltp[2] != '0':
        count1 += 1
    if ltp[4] != '0':
        count1 += 1
	
    if roll in df.index:
        count2 = 0
        for row2 in df.loc[roll, 'course_code']:
            if row2 == sub:
                count2 += 1
        if count1 > count2:
            if count1 != 0:
            	list.append([roll, register, schedule, sub, name, email, aemail, contact])
				
    else:
        if count1 != 0:
            list.append([roll, register, schedule, sub, name, email, aemail, contact])

wb = load_workbook("course_feedback_remaining.xlsx")
sheet = wb.active
for k in list:
    sheet.append(k)
wb.save("course_feedback_remaining.xlsx")