import xlrd
path = r"C:\Users\User\PycharmProjects\pythonProject2\Py_Se_RMG\files\sample.xlsx"

#opening the workbook
wb = xlrd.open_workbook(path)
#getting the handle of the workbook sheet
ws = wb.sheet_by_name("Sheet1")
#getting the data from the rows,interacting with the row
# rows = ws.get_rows() # generator opbject
# print(rows)
# #skipping header
# header = next(rows)
# for row in rows:
#     print(row[0].value,row[1].value)

rows = ws.nrows
d = {}
for i in range(1,rows):
    row = ws.row_values(i)
    d[row[0]] = row[1]
print(d)




