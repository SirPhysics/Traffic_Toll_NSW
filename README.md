# Traffic_Toll_NSW

plt.figure(figsize = (20,6))
sns.set_context('paper', font_scale =1.2)
sns.lineplot(data=traffic_1_df, x="Weekday", y="TotalVolume")
# 1 denotes Sunday
![weekday_traffic](https://user-images.githubusercontent.com/62376291/157602790-7e7d7249-ddf1-4bb7-9b75-4ec92077ef95.png)
