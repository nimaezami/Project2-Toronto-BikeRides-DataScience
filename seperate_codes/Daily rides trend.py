#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Daily rides dataframe
data_daily = pd.DataFrame()
data_daily['rides']=trips_data.groupby('trip_start_time').size().resample('D').sum()
data_daily['annual_members']=trips_data[trips_data['user_type']=='Annual Member'].groupby('trip_start_time').size().resample('D').sum()
data_daily['casual_members']=trips_data[trips_data['user_type']=='Casual Member'].groupby('trip_start_time').size().resample('D').sum()
data_daily.head()

# Visualizing daily rides trend per year 
fig, axes = plt.subplots(2,3,figsize=(20, 15))
data_daily_2017=data_daily.loc['2017']
axes[0, 0].plot(data_daily_2017.index,data_daily_2017["rides"])
axes[0, 0].plot(data_daily_2017.index,data_daily_2017["casual_members"])
axes[0, 0].plot(data_daily_2017.index,data_daily_2017["annual_members"])
axes[0, 0].set_title('Daily ride counts 2017')
axes[0, 0].legend(["Rides","Annual Members","Casual Members"])


data_daily_2018=data_daily.loc['2018']
axes[0, 1].plot(data_daily_2018.index,data_daily_2018["rides"])
axes[0, 1].plot(data_daily_2018.index,data_daily_2018["casual_members"])
axes[0, 1].plot(data_daily_2018.index,data_daily_2018["annual_members"])
axes[0, 1].set_title('Daily ride counts 2018')
axes[0, 1].legend(["Rides","Annual Members","Casual Members"])


data_daily_2019=data_daily.loc['2019']
axes[0, 2].plot(data_daily_2019.index,data_daily_2019["rides"])
axes[0, 2].plot(data_daily_2019.index,data_daily_2019["casual_members"])
axes[0, 2].plot(data_daily_2019.index,data_daily_2019["annual_members"])
axes[0, 2].set_title('Daily ride counts 2019')
axes[0, 2].legend(["Rides","Annual Members","Casual Members"])


data_daily_2020=data_daily.loc['2020']
axes[1, 0].plot(data_daily_2020.index,data_daily_2020["rides"])
axes[1, 0].plot(data_daily_2020.index,data_daily_2020["casual_members"])
axes[1, 0].plot(data_daily_2020.index,data_daily_2020["annual_members"])
axes[1, 0].set_title('Daily ride counts 2020')
axes[1, 0].legend(["Rides","Annual Members","Casual Members"])


data_daily_2021=data_daily.loc['2021']
axes[1, 1].plot(data_daily_2021.index,data_daily_2021["rides"])
axes[1, 1].plot(data_daily_2021.index,data_daily_2021["casual_members"])
axes[1, 1].plot(data_daily_2021.index,data_daily_2021["annual_members"])
axes[1, 1].set_title('Daily ride counts 2021')
axes[1, 1].legend(["Rides","Annual Members","Casual Members"])
plt.setp(axes, xlabel=('Date-Time'), ylabel=("Weekly Trips"))
fig.suptitle('Daily ride counts for Casual Members and Annual Members')

plt.show()

