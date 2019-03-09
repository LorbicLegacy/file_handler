"""
@filename :   excel_code_edit.py
@author: 
name          : Vikas Patel 
internet name : vikaspatelp83
code for creating and editing excel files.

"""
import numpy as np

file = open("data.xls","a")
ids = np.arange(100,105)
data = [92,43,65,23,56]
name = ['Dave','Mark','Joe','John','Linus']

#Now write 
for i in range(len(ids)):
	file.write(f"{ids[i]}\t{name[i]}\t{data[i]}\n")

file.close()

