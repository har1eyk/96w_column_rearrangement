#!C:\Users\harley\AppData\Local\Continuum\anaconda3\python.exe

import pandas as pd
from IPython.display import display

# Break down file name 'C:/Users/harley/Documents/Book2.csv'
# directory = "C:/Users/harley/Documents/"
directory = "S:/NelsonShared/Harley/NelsonLab_EXPERIMENTS/Exp722/"
# file_name = "Book2.csv"
file_name = "PlyC.reduced.conc.w.S.uberis.CWE.repeat.column.export.txt"

# skip header, footer rows. Encoding is important for number interpretation; http://bit.ly/2KsWMl4
df = pd.read_table(directory+file_name, skiprows=17, skipfooter=2, header=0, engine='python', encoding='utf-16')

# last col contains NaN data because line ends in '/t/n' and forms last col when /t del
# first row contains column headers
display (df)

# export in A1, B1, C1 .. A2, B2, C2 format; drop temp col
# change in excel using cells
# ="'"&A1&"', '"&B1&"', '"&C1&"', '"&D1&"', '"&E1&"', '"&F1&"', '"&G1&"', '"&H1&"', "
dfMod = df[['Time', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 
'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 
'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 
'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 
'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 
'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 
'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 
'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 
'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 
'A10', 'B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10', 
'A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11', 
'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'G12', 'H12' 
]]
# view re-arrangement
display (dfMod)

# export re-arranged columns in csv format
file_nameRe = file_name[0:-4]+"_rearranged.csv"
try:
    dfMod.to_csv(directory+file_nameRe)
    print ('Successfully export file:', file_nameRe, ' to location ', directory)
except:
    print ('Failed to export file:', file_nameRe, ' to location ', directory)

