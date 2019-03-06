import openpyxl
import time

t1 = time.time()
print("Begin open file ...")
# load file
wb = openpyxl.load_workbook(filename="./report.xlsx", keep_vba=True)
t2 = time.time()
print("File opened in {0} seconds. Select active sheet ...".format(t2-t1))
# select active sheet
ws = wb.active
print("Modifing value ...")
# modify A1 cell's value
ws['A1'] = 'ABC'
# save file as new xlsx file
t1 = time.time()
print("Saving file ...")
wb.save("abc.xlsx")
t2 = time.time()
print("File saved successfully in {0} seconds!".format(t2-t1))