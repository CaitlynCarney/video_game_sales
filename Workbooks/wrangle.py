import openpyxl
import pandas as pd
import numpy as np


import seaborn as sns
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------------

def acquire_game_sales():
    '''This function takes in dataframe from csv
    returns a pandas dataframe'''
    # pull the file
    wb = openpyxl.load_workbook("vgsales.csv.xlsx")
    ws = wb.active
    # turn into pandas df
    df = pd.DataFrame(list(ws.iter_rows(values_only=True)))
    return df

#-----------------------------------------------------------------------------

def clean_game_sales(df):