 import pandas as pd
 
 def x(a, print_columns=False):
     """
     Extract headers from excel file.

     Args:
        a : path of excel file
        print_colums (boolean): flag if headers should be printed
     Returns:
        headers of excel file
     """
     b = pd.read_excel(a)
     column_headers = list(b.columns.values)
     if print_columns:
         print("\n".join(column_headers))
     return column_headers
