"""
@filename :   excel_code.py
@author: 
name          : Vikas Patel 
internet name : vikaspatelp83
code for creating and editing excel files.

"""
import numpy as np # import for random data
file = open("data.xls","w")
file.write("Id\tName\tData")
file.close()