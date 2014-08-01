import xlrd
import xlwt
import numpy as np

__all__ = ['read_excel', 'write_excel']

def read_excel(filename, n=0):
    """
    Converts a sheet from an Excel file into an ndarray. Assumes all fields are
    numeric values.
    
    Parameters
    ----------
    filename : string
        Path to file.
        
    Returns
    -------
    ndarray with sheet contents.
    """
    contentstring = open(filename, 'rb').read()
    book  = xlrd.open_workbook(file_contents=contentstring)
    sheet = book.sheets()[n]
    array = np.zeros((sheet.ncols, sheet.nrows))
    
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            array[col][row] = sheet.cell(row, col).value
    
    return array

def write_excel(filename, sheetnames, arrays):
    """
    Creates an Excel file with given sheet names and arrays. Assumes all 
    fields are numeric values.
    
    Parameters
    ----------
    filename : string
        Path to file.
    sheetnames : iterable (string)
        List of names for the book's sheets
    arrays : iterable (ndarray)
        List of data arrays for the book's sheets    
    """
    if len(sheetnames) != len(arrays):
        raise IndexError("Array and sheet number must be equal.")
        
    book = xlwt.Workbook()
    
    for name, array in zip(sheetnames, arrays):
        sheet = book.add_sheet(name)
        cols, rows = array.shape
        
        for row in range(rows):
            for col in range(cols):
                sheet.write(row, col, array[col][row])
    
    book.save(filename)
