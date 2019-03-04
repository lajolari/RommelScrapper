import xlwt
from xlwt import Workbook

dic = ['John, john@example.com', 'Mary, mary@example.com', 'John, john@example.com', 'Mary, mary@example.com', 'John, john@example.com', 'Mary, mary@example.com', 'John, john@example.com', 'Mary, mary@example.com'] #dictionary
wb = Workbook()
n = 0
k = 0
sheet1 = wb.add_sheet('Sheet 1') 
for data in dic:
    sheet1.write(n, 0, data)
    n+1

wb.save('clientess.xls')