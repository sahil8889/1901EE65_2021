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
            
            path1 = 'output_by_subject/' + subno + '.csv'
            try: 
                with open(path1):
                    with open(path1, "a") as f1:
                        column=",".join(column)
                        f1.write(column)

            except IOError:
                with open(path1, "w") as f1:
                        f1.write("rollno,register_sem,subno,sub_type\n")
                        column=",".join(column)
                        f1.write(column)
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

            path2 = 'output_individual_roll/' + rollno + '.csv'
            try: 
                with open(path2):
                    with open(path2, "a") as f1:
                        column=",".join(column)
                        f1.write(column)
            except IOError:
                with open(path2, "w") as f1:
                        f1.write("rollno,register_sem,subno,sub_type\n")
                        column=",".join(column)
                        f1.write(column)
        return

output_by_subject()
output_individual_roll()