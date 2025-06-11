'''
Created on 10-Jun-2025

@author: User1
'''
import openpyxl
from openpyxl import Workbook 

filepath = "D:\\YASHU\\work books\\Book1.xlsx"
my_workbook = openpyxl.load_workbook(filepath)
# my_active_sheet = my_workbook.active # Get the currently active sheet
my_active_sheet = my_workbook["Sheet1"]


my_active_sheet.cell(2, 3).value = "pass"

my_workbook.save(filepath)