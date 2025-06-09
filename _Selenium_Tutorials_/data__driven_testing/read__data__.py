'''
Created on 08-Jun-2025

@author: User1
'''
import openpyxl

filepath = "D:\\YASHU\\work books\\Book1.xlsx"
my_workbook = openpyxl.load_workbook(filepath)

my_active_sheet = my_workbook.active
total_rows = my_active_sheet.max_row

print(total_rows)

total_column = my_active_sheet.max_column
print(total_column) 