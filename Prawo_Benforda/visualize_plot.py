import matplotlib as plt
import pyodbc
import pickle
import os

cnxn = pyodbc.connect('Driver={SQL Server};'
                       'Server=DESKTOP-PN31GI1;'
                       'Database=ML;'
                       'Trusted_Connection=yes;')

cursor = cnxn.cursor()
cursor.execute("exec [BenfordFraud].getPotentialFraudulentVendorsList 1")
tables = cursor.fetchall()
for i, table in enumerate(tables):
    fig = pickle.loads(table[11])
    fig.savefig(str(table[0])+'.png')
print("The plots are saved in directory:", os.getcwd())
