import pandas as pd

traffic_df = pd.read_csv("C:\\Users\kcho4\OneDrive\Desktop\Project _Python\Traffic Project\M4_trips_OCT_2021.csv",sep=';')
traffic_df.dtypes
traffic_1_df = pd.DataFrame(traffic_df, columns = ['Date','Weekday','IntervalStart','IntervalEnd',
                                                   'VehicleClass','StartGantryDirection','StartGantryLocation',
                                                   'Lat_Start','Long_Start','StartGantryType','EndGantryDirection',
                                                  'EndGantryLocation','Lat_End','Long_End','EndGantryType','TotalVolume'])
traffic_1_df.head()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style='darkgrid')

plt.figure(figsize=(32,12))
sns.set_style('dark')
sns.set_context('talk')
ax = sns.boxplot(x='IntervalStart',y='TotalVolume',data=traffic_1_df,hue = 'VehicleClass',linewidth=1,fliersize=0.2)
ax_tick = ax.set_xticklabels(ax.get_xticklabels(), rotation=-90)
plt.title('Total Daily Traffic Volume of M4 in 24 hours - Car & Truck Comparison')
plt.xlabel('Timeline')
plt.ylabel("M4's Traffic Volume")

Start_loc = traffic_1_df.pivot_table(index='StartGantryLocation', columns = 'IntervalStart', values = 'TotalVolume')
Start_loc.head()

plt.figure(figsize = (20,6))
sns.set_context('paper', font_scale =1.2)
sns.heatmap(Start_loc,  cmap="YlGnBu", linecolor ='white', linewidth =1 )
plt.title('Total Daily Traffic Volume at all M4 Entry')
plt.xlabel('Time')
plt.ylabel('M4 Entries')

End_loc = traffic_1_df.pivot_table(index='EndGantryLocation', columns = 'IntervalStart', values = 'TotalVolume')
End_loc.head()

plt.figure(figsize = (20,6))
sns.set_context('paper', font_scale =1.2)
sns.heatmap(End_loc,  cmap="BuPu", linecolor ='white', linewidth =1 )
plt.title('Total Daily Traffic Volume at all M4 Exit')
plt.xlabel('Time')
plt.ylabel('M4 Exits')

count_start_df = traffic_1_df.groupby("StartGantryLocation")["TotalVolume"].count()
count_start_df.sum()

count_end_df = traffic_1_df.groupby("EndGantryLocation")["TotalVolume"].count()
count_end_df.sum()

gantrytype_df = traffic_1_df.groupby("StartGantryType")["TotalVolume"].count()
gantrytype_df

plt.figure(figsize = (20,6))
sns.set_context('paper', font_scale =1.2)
sns.lineplot(data=traffic_1_df, x="Weekday", y="TotalVolume")
# 1 denotes Sunday
plt.title('Total Daily Traffic Volume of M4 During Weekdays')
plt.xlabel('Weekdays')
plt.ylabel('Total Traffic Volume')

