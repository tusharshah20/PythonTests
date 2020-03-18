import pandas as pd
sheet = pd.read_excel("I:\GitContent\Datasets\\Bank_fullTest.xlsx")
print(sheet.columns)
print(sheet.head)
print(type(sheet))

