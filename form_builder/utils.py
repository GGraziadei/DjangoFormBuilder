import openpyxl
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd

def generate_excel_report(submissions):
    # Creazione del DataFrame dai dati delle sottomissioni
    data = [submission.submission_data for submission in submissions]
    df = pd.DataFrame(data)
    
    # Creazione di un nuovo file Excel
    wb = Workbook()
    ws = wb.active
    
    # Popolazione delle righe del foglio di lavoro con i dati del DataFrame
    for r_idx, row in enumerate(dataframe_to_rows(df, index=False, header=True), 1):
        for c_idx, value in enumerate(row, 1):
            ws.cell(row=r_idx, column=c_idx, value=value)
    
    # Salva il file Excel
    file_path = "report.xlsx"
    wb.save(file_path)
    return file_path
