import os
def output_by_subject():
    with open('regtable_old.csv','r') as f:
        for line in f:
            x = line.split(',')
            p1 = x[0]
            p2 = x[1]
            p3 = x[3]
            p4 = x[8]
            if(p1=='rollno'):
                continue
            path = 'output_by_subject/'+ p3 + '.csv'
            l=[]
            if(p3 in l):
                with open(path, 'a') as f:
                    f.write(p1 + ',' + p2 + ',' + p3 + ',' + p4)
            else:
                l.append(p3)
                with open(path, 'w') as f:
                    f.write('rollno,' + 'register_sem,' + 'subno,' + 'sub_type\n')
                    f.write(p1 + ',' + p2 + ',' + p3 + ',' + p4)    

    return


def output_individual_roll():
    with open('regtable_old.csv','r') as f:
        for line in f:
            x = line.split(',')
            p1 = x[0]
            p2 = x[1]
            p3 = x[3]
            p4 = x[8]
            if(p1=='rollno'):
                continue
            path = 'output_individual_roll/'+ p1 + '.csv'
            with open(path, 'a') as p:
                p.write('rollno,' + 'register_sem,' + 'subno,' + 'sub_type\n')
                p.write(p1 + ',' + p2 + ',' + p3 + ',' + p4)

    return

output_individual_roll()
output_by_subject()