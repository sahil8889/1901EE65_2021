import os
import csv
import openpyxl

os.mkdir('output_by_subject')
with open('regtable_old.csv', 'r') as csvfile:
    p1 = []
    csvreader = csv.DictReader(csvfile)
    dict = {}
    for column in csvreader:
        l1 = []
        l1.append(column['rollno'])
        l1.append(column['register_sem'])
        l1.append(column['subno'])
        l1.append(column['sub_type'])

        if(column['subno'] in p1):
            dict[column['subno']].append(l1)
        else:
            p1.append(column['subno'])
            dict[column['subno']] = [l1]

for subno in dict:
    path1 = 'output_by_subject/' + subno + '.xlsx'

    wb = openpyxl.Workbook()
    sheet = wb.active
    header = ['rollno', 'register_sem', 'subno', 'sub_type']
    sheet.append(header)

    for column in dict[subno]:
        sheet.append(column)
    wb.save(path1)

os.mkdir('output_individual_roll')
with open('regtable_old.csv', 'r') as csvfile:
    p2 = []
    csvreader = csv.DictReader(csvfile)
    dict = {}
    for column in csvreader:
        l2 = []
        l2.append(column['rollno'])
        l2.append(column['register_sem'])
        l2.append(column['subno'])
        l2.append(column['sub_type'])

        if(column['rollno'] in p2):
            dict[column['rollno']].append(l2)
        else:
            p2.append(column['rollno'])
            dict[column['rollno']] = [l2]

for rollno in dict:
    path2 = 'output_individual_roll/' + rollno + '.xlsx'
    wb = openpyxl.Workbook()
    sheet = wb.active
    header = ['rollno', 'register_sem', 'subno', 'sub_type']
    sheet.append(header)

    for column in dict[rollno]:
        sheet.append(column)
    wb.save(path2)