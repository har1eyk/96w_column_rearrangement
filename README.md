# 96w_column_rearrangement
Python script to re-arrange column format on 96 well plate

# Impetus
96 well plate-reading spectrophotometers like Molecular Devices (MD) readers export data in row format, A1, A2, A3.... Samples in columnar format must be manually manipulated by moving columns together, A1, B1, C1... Data further striated by time series or containing empty columns can be difficult to format for downstream analysis in programs like like Prism, etc.

Column rearrangment can be accomplished manually with spreadsheet programs like Excel, Google Spreadsheets etc. but this a manual process (select column B1, drag to position beside column A1) and prone to errors.

This Python scripts uses Pandas to import data as a dataframe. Column headers kept in row 1 are used as column names e.g. "A1", "A2".."H12".

Once named, columns can be exported in any format, A1, B1, C1, D1..or A1, A2, A3..or A1, 

# Pre-Processing
Pandas can skip over header and footer rows and Molecular Devices (MD) export files do not need pre-processing. However, MD export should be done with "columnar format". Pandas processeds header names.

Files originating elsewhere can be alternatively processed.

Row 1 should contain column names. Extraneous information above row 1 should be removed.
Column export names and formats need to be entered manually in Python program.
I use Excel to rename and enter column-name delimiters. 

```
A1	B1	C1	D1	E1	F1	G1	H1	 	'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 
A2	B2	C2	D2	E2	F2	G2	H2		'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 
A3	B3	C3	D3	E3	F3	G3	H3		'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 
A4	B4	C4	D4	E4	F4	G4	H4		'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 
A5	B5	C5	D5	E5	F5	G5	H5		'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 
A6	B6	C6	D6	E6	F6	G6	H6		'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 
A7	B7	C7	D7	E7	F7	G7	H7		'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 
A8	B8	C8	D8	E8	F8	G8	H8		'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 
A9	B9	C9	D9	E9	F9	G9	H9		'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 
A10	B10	C10	D10	E10	F10	G10	H10		'A10', 'B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10', 
A11	B11	C11	D11	E11	F11	G11	H11		'A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11', 
A12	B12	C12	D12	E12	F12	G12	H12		'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'G12', 'H12', 
```

Here's a template:
```
="'"&A1&"', '"&B1&"', '"&C1&"', '"&D1&"', '"&E1&"', '"&F1&"', '"&G1&"', '"&H1&"', "
```

Paste values and copy to python script. 

I've included a Jupyter notebook to diagnose errors, file locations, etc.
