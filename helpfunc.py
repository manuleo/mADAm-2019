import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from collections import defaultdict

def clean_Fs_and_years(dataframe):
    ''' 
    Cleans columns with title Y----F and removes Y from year column titles
    Input:
        - dataframe (pandas dataframe): dataframe with food balance data for multiple countries
    Output:
        - dataframe (pandas dataframe): updated dataframe after cleaning
    '''
    cols_to_drop = dataframe.columns[dataframe.columns.str.endswith("F")]; #creating a list of columns to be removed
    dataframe = dataframe.drop(columns=cols_to_drop);
    dataframe.columns = dataframe.columns.str.replace("Y","") #rename the columns by deleting "Y" at the beginning
    
    return dataframe

def replace_names_of_countries(dataframe, pairs):
    '''
    Replaces old country names for consistency across different dataframes
    Inputs:
        - dataframe (pandas dataframe): dataframe with food balance data for multiple countries
        - pairs (list): tuples (old, new), where old is going to be replaced by new in the 'Area' part of dataframe
    Output:
        - dataframe (pandas dataframe): updated dataframe after replacements
    '''
    for pair in pairs:
        dataframe['Area'] = dataframe['Area'].replace(pair[0], pair[1])
        
    return dataframe
        
    
def obtain_supply(dataframe_balance):
    '''
    Obtains a dataframe with all lines relative to supply from dataframe (by selecting Item Code = 2901 and Element Code = 664) and drops unecessary data
    Inputs:
        - dataframe_balance (pandas dataframe): dataframe with food balance data for multiple countries
    Outputs:
        - dataframe_supply (pandas dataframe): dataframe with food supply data for multiple countries
    '''
    dataframe_supply = dataframe_balance[(dataframe_balance["Item Code"] == 2901) & (dataframe_balance["Element Code"] == 664)]
    dataframe_supply = dataframe_supply.drop(columns=["Area Code","Item Code","Item","Element Code","Element", "Unit"])
    
    return dataframe_supply

def timeline(dataframe, zone, extras=""):
    '''
    Plots a timeline of food supply in different countries
    Inputs:
        - dataframe (pandas dataframe): dataframe with food supply data for multiple countries
        - zone (str): describes the zone to which countries in the dataframe belong (e.g. "African", "European") [visualization purposes]
        - extras (str): extra information to be displayed in the title of the plot [visualization purposes]
    '''
    dataframe.plot.line(legend = False)
    plt.xlabel("Time (year)", fontsize=18)
    plt.ylabel("Food supply (kcal/person/day)", fontsize=12)
    plt.title("Food supply for different {} countries (Each line is a country){}".format(zone, extras))
    
    
def merge_countries(dataframe, replacements):
    '''
    Merges the history of old countries to their "offspring", in order to smooth out the evolution of one country's supply over the years
    Inputs:
        - dataframe (pandas dataframe): dataframe with food supply data for multiple countries
        - replacements (dictionary): dictionary in the form {old : news}, where old is the previous name for the country or countries listed in news
    Outputs:
        - clean_dataframe (pandas dataframe): dataframe with food supply data for multiple countries (after merging)
    '''
    clean_dataframe = dataframe.copy()
    for old in replacements:
        for new in replacements[old]:
            clean_dataframe[new] += clean_dataframe[old]
        clean_dataframe = clean_dataframe.drop(old, 1) # old country info is no longer necessary
    
    return clean_dataframe

def prepare_future(dataframe, start, end):
    '''
    Appends empty columns for years in the range [start:end] in the columns, in preparation for future analysis
    Input:
        - dataframe (pandas dataframe): dataframe with food supply data for multiple countries
        - start (int): begining of interval to which to create empty columns (inclusive)
        - end (int): end of interval to which to create empty columns (exclusive)
    Outputs:
        - dataframe (pandas dataframe): dataframe with food supply data for multiple countries (after preparation)
    Returns the dataframe with the appended columns
    '''
    dataframe = dataframe.transpose()
    
    for i in np.arange(start,end+1):
        dataframe[i] = np.nan
        
    dataframe = dataframe.transpose()
    
    return dataframe

def single_age(age_range):
    '''
    Given age_range, returns a list of all individual ages in that range
    Input:
        - age_range(str/int/float): age range in formats "x" (single age; type int), "x-y" (multiple ages; type str) or nan (missing value; type float)
    Output:
        - individual_ages (int/lst): a single age (-1 if input is missing value; type int) or a list of single ages (type lst) 
    '''
    res = None
    if type(age_range) ==  float: # nans are the only floats in the age column
        return -1
    elif type(age_range) == int:
        return age_range
    elif re.search('\d-\d', age_range):
        group = age_range.split('-')
        return list(range(int(group[0]), int(group[1])+1))
    elif age_range == "76 and up":
        return list(range(76, 101+1))
    
def explode_age(dataframe):
    '''
    Returns a dataframe where each age_range in dataframe has been expanded across multiple rows.
    Input:
        - dataframe (pandas dataframe): dataframe with caloric need for each age group
    Output:
        - new_dataframe (pandas dataframe): dataframe with caloric need for each individual age
    '''
    accum = []
    for i in dataframe.index:
        row = dataframe.loc[i]
        single = single_age(row['age'])
        if single == -1: # we ignore the nan values, as their rows are empty
            continue
        if type(single) == int:
            accum.append((single, row['input kcal']))
        elif type(single) == list:
            accum.extend([(x, row['input kcal']) for x in single]) 
    return pd.DataFrame(accum, columns=dataframe.columns)

def group(age):
    '''
    Returns the age gruop (groups of 5 ages) to which age belongs, in accordance to population dataset.
    Input:
        - age (int): a single age
    Output:
        - age_group (str): the age group to which age belongs
    '''
    i = int(5*(age//5))
    return "{}-{}".format(i, i+4)

def compress_ages(dataframe):
    '''
    Returns a new dataframe where all ages in dataframe have been grouped, by making an average of all caloric needs for each age in each group.
    Input:
        - dataframe (pandas dataframe): dataframe with caloric need for each individual age
    Output:
        - new_dataframe with caloric need for each age group
    '''
    accum = defaultdict(list)
    for i in dataframe.index:
        row = dataframe.loc[i]
        g_id = group(row['age'])
        if g_id == "100-104":
            g_id = "100+"
        accum[g_id].append(row['input kcal'])
        
    for i in accum:
        accum[i] = sum(accum[i]) / len(accum[i])
        
    return pd.DataFrame.from_dict(accum, orient='index')

def clean_pop_df(dataframe, countries):
    '''
    Returns a dataframe that's been cleaned for the purposes of population analysis. This includes
        dropping unecessary columns, parsing rows referring to the countries we want, as well as 
        multiplying the population by 1000, to obtain the population in units, instead of thousands
        of units.
    Inputs: 
        - dataframe (pandas dataframe): dataframe with information on multiple countries' population
        - countries (list): a list of countries which we want to keep from dataframe
    Outputs:
        - new_dataframe (pandas_dataframe): dataframe with information on countries of interest population, after preprocessing for analysis
    '''     
    #cleaning population dataset
    dataframe.drop(columns=["Index", "Variant", "Notes", "Country code", "Type", "Parent code"], inplace=True)
    dataframe.rename(columns={"Reference date (as of 1 July)": "year", "Region, subregion, country or area *": "country"}, inplace=True)
    
    #keeping only interesting countries
    dataframe = dataframe[dataframe['country'].isin(countries)]
    
    #take into consideration the 1000 of population from the beginning now
    
    dataframe = dataframe.apply(lambda x: x*1000 if x.name not in ['country', 'year'] else x)
    #dataframe.iloc[:, 2:] = dataframe.iloc[:, 2:]*1000
    
    return dataframe

def interpolate_years(dataframe):
    '''
    Interpolation of years' population, which are 5 years apart each.
    Inputs:
        - dataframe (pandas dataframe): dataframe of population for multiple countries (years separated by multiple of 5)
    Outputs:
        - dataframe_yearly (pandas dataframe): dataframe of population for multiple countries after interpolation of years
    '''
    coll = ['country', 'year'] 

    pop_temp= pd.DataFrame(columns = coll)
    dataframe_yearly= pd.DataFrame(columns = coll)
    for country in dataframe.country.drop_duplicates():
        for ages in dataframe.columns[2:]:
            x = dataframe.year.drop_duplicates()
            y = dataframe[(dataframe.country==country)][ages].astype(float)
            xnew = np.arange(1950,2021)
            ynew = np.interp(xnew, x, y, left=None, right=None, period=None)
            pop_temp[ages] = ynew
            pop_temp["country"]=country
            pop_temp["year"]=xnew  
        dataframe_yearly = dataframe_yearly.append(pop_temp, sort=False)
    dataframe_yearly = dataframe_yearly.reset_index().drop(columns="index")
    
    return dataframe_yearly

def obtain_total_pop(male_dataframe, female_dataframe):
    '''
    Accumulates both the male and female population in male/female_dataframe into a new dataframe.
    Input:
        - male_dataframe (pandas dataframe): dataframe of male population for multiple countries
        - female_dataframe (pandas dataframe): dataframe of female population for multiple countries
    Output:
        - pop_total (pandas dataframe): dataframe of total population for multiple countries
    '''
    pop_total = male_dataframe.copy()
    pop_total.iloc[:, 2:] = male_dataframe.iloc[:, 2:] + female_dataframe.iloc[:, 2:]
    sum_ind = pop_total.columns[2:]
    pop_total['Population'] = pop_total[sum_ind].sum(axis=1)
    pop_total.drop(columns=sum_ind, inplace=True)
    return pop_total

def reshape_pop_dataframe(dataframe):
    '''
    Reshape a dataframe to be similar in format to other datasets used, in other to allow comparisons of the two.
    Input:
        - dataframe (pandas dataframe): dataframe with population information for multiple countries
    Output:
        - reshaped_dataframe (pandas daframe): reshaped dataframe with population information for multiple countries
    '''
    # We sort values by year, we group them by country and we tranpose the values in columns Population.
    # In the function lambda we reset the index. The unstack() allows to return a new dataframe with 
    # a new level of columns.
    years = list(dataframe.year.drop_duplicates().sort_values())
    dataframe = dataframe.sort_values('year').groupby("country")['Population'].apply(lambda df: df.reset_index(drop=True)).unstack()
    dataframe.columns = years
    dataframe.index.name = 'Country'
    
    return dataframe

def get_calories(dataframe, need):
    '''
    Returns a dataframe with caloric needs per country.
    Inputs:
        - dataframe (pandas dataframe): dataframe with population information for multiple countries (refers to one gender)
        - need (pandas dataframe): dataframe with caloric need information per age group (refers to one gender)
    Output:
        - cal_demand (pandas dataframe): dataframe with caloric needs for each country, each year and per age group (refers to one gender)
    '''
    df_mult = dataframe.drop(columns=["country", "year"]) # used only for multiply function
    cal_demand = df_mult.multiply(need.squeeze()) # squeeze adapts the dimension of the dataframe
    cal_demand.insert(0,"country",dataframe.country)
    cal_demand.insert(1,"year",dataframe.year)
    
    return cal_demand

def obtain_total_cal_need(male_dataframe, female_dataframe):
    '''
    Returns the sum of caloric needs for both male and female populations, obtaining the full population
        caloric needs in each country.
    Inputs:
        - male_dataframe (pandas dataframe): dataframe with caloric needs for male population in multiple countries
        - female_dataframe (pandas dataframe): dataframe with caloric needs for female population in multiple countries
    Output:
        - total_cal_demand (pandas dataframe): dataframe with caloric needs for each country, each year and per age group
    '''
    total_cal_demand = male_dataframe.copy()
    sum_ind = total_cal_demand.columns[2:]
    total_cal_demand[sum_ind] = total_cal_demand[sum_ind] + female_dataframe[sum_ind]
    
    return total_cal_demand

def obtain_difference(pop_dataframe, supply_dataframe, total_cal_demand):
    '''
    Returns the difference between supply and demand in caloric need for a specific zone of the world
    Inputs:
        - pop_dataframe (pandas dataframe): dataframe with population data for multiple countries
        - supply_dataframe (pandas dataframe): dataframe with information about food supply for multiple countries 
        - total_cal_demand (pandas dataframe): dataframe with information about total caloric demand for multiple countries
    Outputs:
        - cal_difference (pandas dataframe): dataframe with difference between available supply and actual demand (of calories) for multiple countries
    '''
    supply_dataframe_cpy = supply_dataframe.transpose()
    supply_dataframe_cpy = supply_dataframe_cpy*365
    
    pop_to_mult = pop_dataframe.copy()
    supply_to_mult = supply_dataframe_cpy.copy()
    supply_final = pop_to_mult.multiply(supply_to_mult)    

    supply_final = supply_final.dropna(axis=1, how="all")
    
    cal_difference = (supply_final - total_cal_demand)/365
    cal_difference = cal_difference.div(pop_to_mult).dropna(axis=1, how="all")
    cal_difference = cal_difference.dropna(axis=0, how="all")
    
    return cal_difference