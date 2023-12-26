import openpyxl
wb = openpyxl.load_workbook("Price.xlsx")

wb.copy_worksheet(wb['new'])
ws
wb.save("Price.xlsx")


