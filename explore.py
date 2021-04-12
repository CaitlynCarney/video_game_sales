import pandas as pd
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.axes as ax
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import wrangle

import warnings
warnings.filterwarnings("ignore")

np.set_printoptions(suppress=True)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
df = wrangle.acquire_game_sales()
df = wrangle.clean_game_sales(df)
train, validate, test = wrangle.split_game_sales(df)
X_train, X_validate, X_test, y_train, y_validate, y_test = wrangle.split_train_validate_test(train, validate, test)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def see_success_through_years(train):
    '''This function takes in train
    returns 4 barplots of each success level
    sees them through the years'''
    plt.subplots(2, 2, figsize=(40,16), sharey=True)
    sns.set(style="darkgrid")
    # plot moderate success
    plt.subplot(2,2,1)
    plt.title("Moderate Successful Games Through the Years", size=20, color='black')
    sns.barplot(y='Moderate_Success', x ='years_binned', data = train, palette='hot')
    # plot Fairly successful
    plt.subplot(2,2,2)
    plt.title("Fairly Successful Games Through the Years", size=20, color='black')
    sns.barplot(y='Fairly_Successful', x ='years_binned', data = train, palette='hot')
    # plot Very successful
    plt.subplot(2,2,3)
    plt.title("Very Successful Games Through the Years", size=20, color='black')
    sns.barplot(y='Very_Successful', x ='years_binned', data = train, palette='hot')
    # plot extremely successful
    plt.subplot(2,2,4)
    plt.title("Extremely Successful Games Through the Years", size=20, color='black')
    sns.barplot(y='Extremely_Successful', x ='years_binned', data = train, palette='hot')
see_success_through_years(train)

def success_percent_per_platform(train):
    '''This funciton take in the train date
    creates bar plot for each platform
    shows the percent of each platforms influence on each success level'''
    plt.subplots(2, 3, figsize=(40,16), sharey=True)
    sns.set(style="darkgrid")
    #plot nintendo
    plt.subplot(2,3,1)
    plt.title("Perent of Sales for Nintendo Platforms", size=20, color='black')
    sns.barplot(y='Nintendo', x='level_of_success', data=train,
                   palette='hot')
    # plot playstation
    plt.subplot(2,3,2)
    plt.title("Percent of Sales for Playstation Platforms", size=20, color='black')
    sns.barplot(y='Playstation', x='level_of_success', data=train,
                   palette='hot')
    # plot Xbox
    plt.subplot(2,3,3)
    plt.title("Percent of Sales for Xbox Platforms", size=20, color='black')
    sns.barplot(y='Xbox', x='level_of_success', data=train,
                   palette='hot')
    # plot computer
    plt.subplot(2,3,4)
    plt.title("Percent of Sales for Computer Platforms", size=20, color='black')
    sns.barplot(y='Computer', x='level_of_success', data=train,
                   palette='hot')
    # plot sega
    plt.subplot(2,3,5)
    plt.title("Percent of Sales for Sega Platforms", size=20, color='black')
    sns.barplot(y='Sega', x='level_of_success', data=train,
                   palette='hot')
    # plot all others
    plt.subplot(2,3,6)
    plt.title("Percent of Sales for All Other Platforms", size=20, color='black')
    sns.barplot(y='Other', x='level_of_success', data=train,
                   palette='hot')

    
def success_percent_per_genre(train):
    plt.subplots(2, 4, figsize=(55,16), sharey=True)
    sns.set(style="darkgrid")
    # plot action adventer
    plt.subplot(2,4,1)
    plt.title("Perent of Sales for Action Adventure Games", size=20, color='black')
    sns.barplot(y='Action_Adventure', x='level_of_success', data=train,
                   palette='hot')
    # plot simulation
    plt.subplot(2,4,2)
    plt.title("Percent of Sales for Simulation Games", size=20, color='black')
    sns.barplot(y='Simulation', x='level_of_success', data=train,
                   palette='hot')
    # plot sports
    plt.subplot(2,4,3)
    plt.title("Percent of Sales for Sports Games", size=20, color='black')
    sns.barplot(y='Sports', x='level_of_success', data=train,
                   palette='hot')
    # plot RPG
    plt.subplot(2,4,4)
    plt.title("Percent of Sales for RPG's", size=20, color='black')
    sns.barplot(y='Role_Playing', x='level_of_success', data=train,
                   palette='hot')
    # plot Shooter
    plt.subplot(2,4,5)
    plt.title("Percent of Sales for Shooter Games", size=20, color='black')
    sns.barplot(y='Shooter', x='level_of_success', data=train,
                   palette='hot')
    # plot Strategy
    plt.subplot(2,4,6)
    plt.title("Percent of Sales for Strategy Games", size=20, color='black')
    sns.barplot(y='Strategy', x='level_of_success', data=train,
                   palette='hot')
    # plot misc
    plt.subplot(2,4,7)
    plt.title("Percent of Sales for All Other Game Types", size=20, color='black')
    sns.barplot(y='Misc', x='level_of_success', data=train,
                   palette='hot')
    

def genre_stat_test(train):
    '''conducts chi square test on genre and success level'''
    # normlaize makes it percentage
    observe = pd.crosstab(train.Genre, train.level_of_success, margins = True)
    chi2, p, degf, expected = stats.chi2_contingency(observe)
    # Chi test is for catigorical vs catigorical
    null_hypothesis = "A games genre and its level of success are independent from each other"
    alt_hypothesis = "The genre of a game and its success are dependent on one another."
    alpha = .05 #my confident if 0.95 therfore my alpha is .05

    if p < alpha:
        print("I reject the null hypothesis")
        print("I reject the hypothesis that: \n", null_hypothesis)
        print(' ')
        print(f'The alpha is: \n', alpha)
        print(' ')
        print(f'P Value is: \n', p)
    else:
        print("I fail to reject the null hypothesis")
        print("There is not enough evidence to move forward with the alternative hypothesis")
        print(f'P Value is: \n', p)
        print(' ')
        print(f'P Value is: \n', alpha)
        
        
def year_stat_test(train):
    '''conducts chi square test on years binned and success level'''
    # normlaize makes it percentage
    observe = pd.crosstab(train.years_binned, train.level_of_success, margins = True)
    chi2, p, degf, expected = stats.chi2_contingency(observe)
    # Chi test is for catigorical vs catigorical
    null_hypothesis = "A games release year and its level of success are independent from each other"
    alt_hypothesis = "The release year of a game and its success are dependent on one another."
    alpha = .05 #my confident if 0.95 therfore my alpha is .05

    if p < alpha:
        print("I reject the null hypothesis")
        print("I reject the hypothesis that: \n", null_hypothesis)
        print(' ')
        print(f'The alpha is: \n', alpha)
        print(' ')
        print(f'P Value is: \n', p)
    else:
        print("I fail to reject the null hypothesis")
        print("There is not enough evidence to move forward with the alternative hypothesis")
        print(f'P Value is: \n', p)
        print(' ')
        print(f'P Value is: \n', alpha)
        
def platform_stat_test(train):
    '''conducts chi square test on platform and success level'''
    # normlaize makes it percentage
    observe = pd.crosstab(train.Platform, train.level_of_success, margins = True)
    chi2, p, degf, expected = stats.chi2_contingency(observe)
    # Chi test is for catigorical vs catigorical
    null_hypothesis = "A games platform and its level of success are independent from each other"
    alt_hypothesis = "The platform of a game and its success are dependent on one another."
    alpha = .05 #my confident if 0.95 therfore my alpha is .05

    if p < alpha:
        print("We reject the null hypothesis")
        print("We reject the hypothesis that: \n", null_hypothesis)
        print(' ')
        print(f'The alpha is: \n', alpha)
        print(' ')
        print(f'P Value is: \n', p)
    else:
        print("I fail to reject the null hypothesis")
        print("There is not enough evidence to move forward with the alternative hypothesis")
        print(f'P Value is: \n', p)
        print(' ')
        print(f'P Value is: \n', alpha)