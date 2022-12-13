from xlrd import open_workbook

def read_locators(sheetname):
    objects = { }
    wb = open_workbook("../Data_files/objects.xls")
    #. will show currently wer it is . it go backward give forward slash(/) control space
    ws = wb.sheet_by_name(sheetname)
    # "nrows" returns total number of used rows in the excel
    rows = ws.nrows
    for i in range(1, rows):   # range(1, 4)
        data = ws.row_values(i)
        objects[data[0]] = (data[1], data[2])
    return objects


def read_headers(sheetname, testcasename):
    wb = open_workbook("../Data_files/testdata.xls")
    ws = wb.sheet_by_name(sheetname)
    rows = ws.nrows
    for i in range(0, rows):   # range(0, 16)
        temp = ws.row_values(i)
        # print(temp)
        if temp[0] == testcasename:

            # the row number of the testcase will be one less than the row where actual testdata is starting
            headers = ws.row_values(i-1) #here i will be 1
            # print(headers)

            _headers = [ item for item in headers if item.strip() ]
            _headers = ",".join(_headers[2:])
            return _headers
            
def read_data(sheetname, testcasename):
    wb = open_workbook("../Data_files/testdata.xls")
    ws = wb.sheet_by_name(sheetname)
    rows = ws.nrows
    final_data = [ ]
    for i in range(0, rows):   # range(0, 16)
        temp = ws.row_values(i)

        if temp[0] == testcasename:
            data = ws.row_values(i)
            #print(data)
            data = [ item for item in data if item ]
            data = [ item for item in data if data[1] == "Yes" ]
            if data:
                final_data.append(tuple(data[2:]))
    return final_data

#print(read_locators("registrationpage"))
# print(read_headers("shopping","test_login_positive"))
# print(read_data("shopping","test_login_positive"))
























































