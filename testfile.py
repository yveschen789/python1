import csv
import xlrd
import pandas as pd

sheet = xlrd.open_workbook('../data.yml').sheet_by_index(0)
print(sheet)
