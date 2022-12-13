import xlrd
path_ = r"C:\Users\User\OneDrive\Desktop\data_file.xlsx"
#path = r"C:\Users\User\PycharmProjects\pythonProject2\skillrary\data\data_file.xlsx"

"""
def read_locators():
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name("loginpage")
    rows = worksheet.get_rows()
    print(rows) # gives generator object
    header = next(rows)
    for row in rows:
        print(row[0].value,row[1].value,row[1].value,row[2].value)


#read_locators()

"""
def read_locators():
    workbook = xlrd.open_workbook(path_)
    worksheet = workbook.sheet_by_name("loginpage")
    rows = worksheet.nrows # gives the length of rows
    #print(rows)
    d = {}
    for i in range(1,rows):
        row = worksheet.row_values(i)
        d[row[0]] = (row[1],row[2])
    return d
#print(read_locators())

