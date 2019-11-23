# -*- coding: utf-8 -*-

"""Plot functions"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from folium import plugins
plt.rcParams["figure.figsize"] = (15,8) #set size of plot


def timeline_supply(dataframe, zone, extras=""):
    '''
    Plots a timeline of food supply in different countries
    Inputs:
        - dataframe (pandas dataframe): dataframe with food supply data for multiple countries
        - zone (str): describes the zone to which countries in the dataframe belong (e.g. "African", "European") [visualization purposes]
        - extras (str): extra information to be displayed in the title of the plot [visualization purposes]
    '''
    dataframe.plot.line(legend = False)
    plt.xlabel("Time (year)")
    plt.ylabel("Food supply (kcal/person/day)")
    plt.title("Food supply for different {} countries (Each line is a country){}".format(zone, extras))
    
def plot_map(dataframe, geo_world_path, country_codes, colorbrew, legend_name, value_description):
    '''
    Plot a choropleth map (geographic heat map), implementing tooltips showing name of the countries and the values passed in dataframe.
    Inputs:
        - dataframe (pandas dataframe): dataframe containing a column with the values to plot in the choropleth for each country
        - geo_world_path (string): path to the json with coordinates for all the country in the word (geometries)
        - country_codes (list): countries to retain from the world in the plot
        - colorblew (string): color palette to use in the map
        - legend_name (string): name in the legend of the colors
        - value_description (string): description of the value presented in the map
    Output:
        - mymap: map that will be plotted'''
    
    #Preparing data to plot
    geojson_world = gpd.read_file(geo_world_path) 
    geojson_continent = geojson_world[geojson_world.id.isin(country_codes)] #retaining interested countries from "country_codes" list
    data_plot = geojson_continent.sort_values(by="name").copy() # sorting by name to match the country codes
    data_plot["val"] = dataframe.values #adding values to plot from "dataframe"
    
    #Preparing plot
    x_map=data_plot.centroid.x.mean() #Center map
    y_map=data_plot.centroid.y.mean()
    mymap = folium.Map(location=[y_map, x_map], zoom_start=3, tiles=None) #Initialize map
    tiles = "https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png" #Type of map
    folium.TileLayer(tiles,subdomains = "abc", attr=" " ,name="Light Map",control=False).add_to(mymap); #Apply type of map to "mymap"
    
    #Creating Choropleth map
    mymap.choropleth(
        geo_data=data_plot,
        name='Choropleth',
        data=data_plot,
        columns=['id','val'],
        key_on="feature.properties.id",
        fill_color=colorbrew,
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=legend_name,
        smooth_factor=0.1
    )
    #Style and Highlight function for tooltip
    style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}
    highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1}
    
    #Creating tooltip activating on hoover
    tooltips = folium.features.GeoJson(
        data_plot,
        style_function=style_function, 
        control=False,
        highlight_function=highlight_function, 
        tooltip=folium.features.GeoJsonTooltip(
        fields=['name','val'],
        aliases=['Country: ',value_description],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
        )
    )
    
    mymap.add_child(tooltips)
    mymap.keep_in_front(tooltips)
    folium.LayerControl().add_to(mymap)
    return mymap

def draw_demand_bar(current_year, cal_demand):
    '''
    Plot a combination of the barchart with the share of country in surplus/deficit of kcal/person/day
    Input:
        - current_year (int): year to plot
        - cal_demand (pandas dataframe): dataframe with kcal demand for interested countries
    '''
    # clear plot and define grid
    plt.clf();
    grid = plt.GridSpec(1, 5, wspace=0.4, hspace=0.3);
    cal_sorted = cal_demand[current_year].sort_values()
    
    # first bar plot 
    plt.subplot(grid[0, 1:4]);
    p = cal_sorted.plot(kind='barh', color=(cal_sorted > 0).map({True: 'g', False: 'red'}),alpha=0.75, rot=0);
    plt.title('Food availability', fontsize=20, weight = 'bold');
    p.set_xlabel(" Excess Calories [kcal/persona/day]", weight = 'bold');
    p.set_ylabel("African countries", weight = 'bold', fontsize=16);
    plt.xlim([-1000,1400]);
    plt.text(800,1,current_year, fontsize=40, weight = 'bold');
    
    # new plot with sum of countries with excess or deficit
    deficit = len(cal_demand[cal_demand[current_year].values < 0].index)
    excess = len(cal_demand[cal_demand[current_year].values >= 0].index)
    ax2 = plt.subplot(grid[0, 4]);
    plt.bar("Countries", deficit, 0.01, color='red', alpha=0.75);
    plt.bar("Countries", excess, 0.01, bottom=deficit, color='g', alpha=0.75);
    plt.yticks([]);
    plt.xticks([]);
    plt.title("Share", fontsize=16, weight = 'bold');
    ax2.axis('off');
    
    # share info
    deficit_share = int(deficit/(deficit+excess)*100)
    excess_share = int(excess/(deficit+excess)*100)
    plt.text(0,2, str(deficit_share) + " %", fontsize=20, weight = 'bold', horizontalalignment="center");
    plt.text(0,38, str(excess_share) + " %", fontsize=20, weight = 'bold', horizontalalignment="center");
    