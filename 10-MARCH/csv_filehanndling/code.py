import csv
from datetime import date
file=open('expense.csv','a+',newline='')
w=csv.writer(file)
r=csv.reader(file)
file.seek(0)
print(list(r))
# w.writerow(['DATE','CATEGORY','AMOUNT']) #prefer to use writerow to provide column name
#writerows used for data 
# w.writerows([
#     [date.today(),'Travel',2000],
#     [date.today(),'Food',1000],
#     [date.today(),'Entertainment',1000]
# ])
# r=csv.reader(file)


file.close()