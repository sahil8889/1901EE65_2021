import os

def output_by_subject():
    os.mkdir('output_by_subject')
    file = "regtable_old.csv"    
    with open(file, "r") as f:
        for line in f:
            column = line.split(',')
            subno=column[3]
            del column[4:8]
            del column[2]
            if (column[3] =="subno"):
                continue
            
            path1 = 'output_by_subject/' + subno + '.xlsx'
            try: 
                from openpyxl import load_workbook
                wb = load_workbook(path1)
                sheet1 = wb.active
                wb.save(path1)

            except IOError:
                from openpyxl import Workbook
                wb = Workbook()
                sheet1 = wb.active
                sheet1.append(['rollno','register_sem','subno','sub_type'])
                sheet1.append(column)
                wb.save(path1)
        return

def output_individual_roll():
    os.mkdir('output_individual_roll')
    file = "regtable_old.csv"
    with open(file, "r") as f:
        for line in f:
            column = line.split(',')
            rollno=column[0]
            del column[4:8]
            del column[2]
            if (column[0] =="rollno"):  
                continue

            path2 = 'output_individual_roll/' + rollno + '.xlsx'
            try: 
                from openpyxl import load_workbook
                wb = load_workbook(path2)
                sheet1 = wb.active
                sheet1.append(column)
                wb.save(path2)
            except IOError:
                from openpyxl import Workbook
                wb = Workbook()
                sheet1 = wb.active
                sheet1.append(['rollno','register_sem','subno','sub_type'])
                sheet1.append(column)
                wb.save(path2)
        return

output_by_subject()
output_individual_roll()