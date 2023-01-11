import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def visualise_traffic_data(data_file):
    # read in the data file
    traffic_df = pd.read_csv(data_file, sep=';')

    # select only the relevant columns
    traffic_df = traffic_df[['Date','Weekday','IntervalStart','IntervalEnd',
                             'VehicleClass','StartGantryDirection','StartGantryLocation',
                             'Lat_Start','Long_Start','StartGantryType','EndGantryDirection',
                             'EndGantryLocation','Lat_End','Long_End','EndGantryType','TotalVolume']]

    # set seaborn plotting style
    sns.set_theme(style='darkgrid')
    sns.set_style('dark')
    sns.set_context('talk')
    
    # create a boxplot to compare traffic volume by vehicle class
    plt.figure(figsize=(32,12))
    ax = sns.boxplot(x='IntervalStart', y='TotalVolume', data=traffic_df, hue='VehicleClass', linewidth=1, fliersize=0.2)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=-90)
    plt.title('Total Daily Traffic Volume of M4 in 24 hours - Car & Truck Comparison')
    plt.xlabel('Timeline')
    plt.ylabel("M4's Traffic Volume")
    
    # create a heatmap to visualise traffic volume by entry location
    Start_loc = traffic_df.pivot_table(index='StartGantryLocation', columns='IntervalStart', values='TotalVolume')
    plt.figure(figsize=(20,6))
    sns.set_context('paper', font_scale=1.2)
    sns.heatmap(Start_loc, cmap='YlGnBu', linecolor='white', linewidth=1)
    plt.title('Total Daily Traffic Volume at all M4 Entry')
    plt.xlabel('Time')
    plt.ylabel('M4 Entries')
    
    # create a heatmap to visualise traffic volume by exit location
    End_loc = traffic_df.pivot_table(index='EndGantryLocation', columns='IntervalStart', values='TotalVolume')
    plt.figure(figsize=(20,6))
    sns.set_context('paper', font_scale=1.2)
    sns.heatmap(End_loc, cmap='BuPu', linecolor='white', linewidth=1)
    plt.title('Total Daily Traffic Volume at all M4 Exit')
    plt.xlabel('Time')
    plt.ylabel('M4 Exits')
    
    # create a line plot to visualise traffic volume by day of the week
    plt.figure(figsize=(20,6))
    sns.set_context('paper', font_scale=1.2)
    sns.lineplot(data=traffic_df, x='Weekday', y='TotalVolume')
    plt.title('Total Daily Traffic Volume of M4 During Weekdays')
    plt.xlabel('Weekdays')
    plt.ylabel('M4 Traffic Volume')
    
    # count the number of observations for each start location
    count_start_df = traffic_df.groupby('StartGantryLocation')['TotalVolume'].count()
    print('Number of observations for each start location:')
    print(count_start_df)
    print('Total number of observations for start locations:', count_start_df.sum())
    
    # count the number of observations for each end location
    count_end_df = traffic_df.groupby('EndGantryLocation')['TotalVolume'].count()
    print('Number of observations for each end location:')
    print(count_end_df)
    print('Total number of observations for end locations:', count_end_df.sum())
    
    # count the number of observations for each gantry type
    gantrytype_df = traffic_df.groupby('StartGantryType')['TotalVolume'].count()
    print('Number of observations for each gantry type:')
    print(gantrytype_df)

# use the function to visualise the traffic data
visualise_traffic_data('data.csv')

