import openpyxl
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

import sklearn.preprocessing
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.datasets.samples_generator import make_blobs

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
    '''This function take in a dataframe
    moves column names from rows to the columns
    drops the row with the column names
    drops columns from Year column where variable is N/A
    changes Year and Sales to int/float
    drops cheating columns
    bin the year column
    push together varaibles from platform and genre to minimize dummies
    create dummies
    concats dummys to df
    returns dataframe'''
    # Set the column names 
    # had to do this because column names became first row
    df.columns = df.iloc[0]
    # set the index of the dataframe
    df = df.set_index('Rank')
    # drop the row with column names
    df = df.drop('Rank', axis=0)
    # drop N/A values
    df = df[~df['Year'].isin(['N/A'])]
    # Change data types
    df['Year'] = df['Year'].astype(int)
    df['Global_Sales'] = df['Global_Sales'].astype(float)
    # dropping these because they feed right into our target and Name is not needed
    df = df.drop(['NA_Sales', 'EU_Sales', 
                 'JP_Sales', 'Other_Sales', 'Name'], axis=1)
    # bin the year column to help exploration
    df['years_binned'] = pd.cut(df.Year, 
                                bins = [1980,1985,1990,1995,2000,2005,2010,2015,2020],
                                labels = ['80-85', '85-90', '90-95', "95-00's", 
                                          "00's-05", '05-10', '10-15', '15-20'])
    # bin the year column to help exploration
    df['level_of_success'] = pd.cut(df.Global_Sales, 
                        bins = [0,0.1,0.5,0.9,100],
                        labels = ['Moderate Success', 'Fairly Successful', 'Very Successful', 
                                  'Extremely Successful'])
    # Sony
    df['Platform'] = df.Platform.replace('PS2','Playstation')
    df['Platform'] = df.Platform.replace('PS3','Playstation')
    df['Platform'] = df.Platform.replace('PSP','Playstation')
    df['Platform'] = df.Platform.replace('PS','Playstation')
    df['Platform'] = df.Platform.replace('PS4','Playstation')
    # Xbox
    df['Platform'] = df.Platform.replace('X360','Xbox')
    df['Platform'] = df.Platform.replace('XB','Xbox')
    df['Platform'] = df.Platform.replace('XOne','Xbox')
    # Nintendo
    df['Platform'] = df.Platform.replace('DS','Nintendo')
    df['Platform'] = df.Platform.replace('Wii','Nintendo')
    df['Platform'] = df.Platform.replace('GB','Nintendo')
    df['Platform'] = df.Platform.replace('GC','Nintendo')
    df['Platform'] = df.Platform.replace('3DS','Nintendo')
    df['Platform'] = df.Platform.replace('SNES','Nintendo')
    df['Platform'] = df.Platform.replace('WiiU','Nintendo')
    df['Platform'] = df.Platform.replace('NES','Nintendo')
    df['Platform'] = df.Platform.replace('Gameboy','Nintendo')
    df['Platform'] = df.Platform.replace('N64','Nintendo')
    df['Platform'] = df.Platform.replace('SCD','Nintendo')
    df['Platform'] = df.Platform.replace('GBA','Nintendo')
    # Computer
    df['Platform'] = df.Platform.replace('PC','Computer')
    df['Platform'] = df.Platform.replace('PSV','Computer')
    # Sega
    df['Platform'] = df.Platform.replace('SAT','Sega')
    df['Platform'] = df.Platform.replace('DC','Sega')
    df['Platform'] = df.Platform.replace('GEN','Sega')
    df['Platform'] = df.Platform.replace('GG','Sega')
    # Other
    df['Platform'] = df.Platform.replace(2600,'Other')
    df['Platform'] = df.Platform.replace('NG','Other')
    df['Platform'] = df.Platform.replace('WS','Other')
    df['Platform'] = df.Platform.replace('3DO','Other')
    df['Platform'] = df.Platform.replace('TG16','Other')
    df['Platform'] = df.Platform.replace('PCFX','Other')
    # replace genres
    df['Genre'] = df.Genre.replace('Puzzle','Strategy')
    df['Genre'] = df.Genre.replace('Action','Action_Adventure')
    df['Genre'] = df.Genre.replace('Adventure','Action_Adventure')
    df['Genre'] = df.Genre.replace('Fighting','Simulation')
    df['Genre'] = df.Genre.replace('Racing','Simulation')
    df['Genre'] = df.Genre.replace('Role-Playing','Role_Playing')
    # create dummy variables for platform and add them to the df
    dummy_df =  pd.get_dummies(df['Platform'])
    dummy_df.columns = ['Nintendo', 'Playstation', 'Xbox', 'Computer', 
                        'Sega', 'Other']
    df = pd.concat([df, dummy_df], axis=1)
    # create dummy variables for genre and add them to the df
    dummy_df =  pd.get_dummies(df['Genre'])
    dummy_df.columns = ['Action_Adventure', 'Simulation', 'Sports', 
                        'Misc', 'Role_Playing', 'Shooter', 
                        'Strategy', 'Platform']
    df = pd.concat([df, dummy_df], axis=1)
    # create dummy variables for success level
    dummy_df =  pd.get_dummies(df['level_of_success'])
    dummy_df.columns = ['Moderate_Success', 'Fairly_Successful', 'Very_Successful', 
                                  'Extremely_Successful']
    df = pd.concat([df, dummy_df], axis=1)
    # Rename columns
    df.columns = ['Platform','Year', 'Genre', 'Publisher', 'Global_Sales', 'years_binned', 
              'level_of_success', 'Nintendo', 'Playstation' ,'Xbox', 'Computer', 
              'Sega', 'Other', 'Action_Adventure', 'Simulation', 'Sports', 
              'Misc', 'Role_Playing', 'Shooter', 'Strategy', 'Plat', 
              'Moderate_Success', 'Fairly_Successful', 'Very_Successful', 
              'Extremely_Successful']
    #drop features
    df = df.drop(['Plat'], axis=1)
    return df

#-----------------------------------------------------------------------------

# Split the Data into Tain, Test, and Validate.

def split_game_sales(df):
    '''This fuction takes in a df 
    splits into train, test, validate
    return: three pandas dataframes: train, validate, test
    '''
    # split the focused zillow data
    train_validate, test = train_test_split(df, test_size=.2, random_state=1234)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                       random_state=1234)
    return train, validate, test

# Split the data into X_train, y_train, X_vlaidate, y_validate, X_train, and y_train

def split_train_validate_test(train, validate, test):
    ''' This function takes in train, validate and test
    splits them into X and y versions
    returns X_train, X_validate, X_test, y_train, y_validate, y_test'''
    X_train = train.drop(columns = ['level_of_success'])
    y_train = pd.DataFrame(train.level_of_success)
    X_validate = validate.drop(columns=['level_of_success'])
    y_validate = pd.DataFrame(validate.level_of_success)
    X_test = test.drop(columns=['level_of_success'])
    y_test = pd.DataFrame(test.level_of_success)
    return X_train, X_validate, X_test, y_train, y_validate, y_test

#-----------------------------------------------------------------------------

# Scale the Data

def scale_my_data(train, validate, test):
    scale_columns = ['Global_Sales', 'Year']
    scaler = MinMaxScaler()
    scaler.fit(train[scale_columns])

    train_scaled = scaler.transform(train[scale_columns])
    validate_scaled = scaler.transform(validate[scale_columns])
    test_scaled = scaler.transform(test[scale_columns])
    #turn into dataframe
    train_scaled = pd.DataFrame(train_scaled)
    validate_scaled = pd.DataFrame(validate_scaled)
    test_scaled = pd.DataFrame(test_scaled)
    
    return train_scaled, validate_scaled, test_scaled

#-----------------------------------------------------------------------------

# Focused Data

def focused_game_sales(df):
    '''
    takes in train
    sets sepecific features to focus on
    returns a focused data frame in a pandas dataframe
    '''
    # choose features to focus on
    features = [
    'Year','level_of_success',
    'Nintendo','Playstation','Xbox','Computer','Sega','Other',
    'Action_Adventure', 'Simulation', 'Sports', 'Misc', 'Role_Playing', 'Shooter',
    'Strategy'] 
    # the target is level of success
    # return a df based only on these features
    df2 = df[features]
    return df2

def split_focused_game_sales(df2):
    '''This fuction takes in a df 
    splits into train, test, validate
    return: three pandas dataframes: train, validate, test
    '''
    # split the focused zillow data
    train_validate2, test2 = train_test_split(df2, test_size=.2, random_state=1234)
    train2, validate2 = train_test_split(train_validate2, test_size=.3, 
                                       random_state=1234)
    return train2, validate2, test2

def split_train2_validate2_test2(train2, validate2, test2):
    ''' This function takes in train, validate and test
    splits them into X and y versions
    returns X_train, X_validate, X_test, y_train, y_validate, y_test'''
    X_train = train.drop(columns = ['level_of_success'])
    y_train = pd.DataFrame(train.level_of_success)
    X_validate = validate.drop(columns=['level_of_success'])
    y_validate = pd.DataFrame(validate.level_of_success)
    X_test = test.drop(columns=['level_of_success'])
    y_test = pd.DataFrame(test.level_of_success)
    return X_train2, X_validate2, X_test2, y_train2, y_validate2, y_test2