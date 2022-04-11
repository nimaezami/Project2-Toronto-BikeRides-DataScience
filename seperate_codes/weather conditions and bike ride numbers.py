#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#relationship between weather conditions and bike ride numbers
hourly_rides_and_weather = pd.DataFrame()
hourly_rides_and_weather['rides']=data_merged.groupby('trip_start_time').size().resample('D').sum()
hourly_rides_and_weather['annual_members']=data_merged[data_merged['user_type']=='Annual Member'].groupby('trip_start_time').size().resample('D').sum()
hourly_rides_and_weather['casual_members']=data_merged[data_merged['user_type']=='Casual Member'].groupby('trip_start_time').size().resample('D').sum()
hourly_rides_and_weather['workday']='False'
hourly_rides_and_weather['day']= hourly_rides_and_weather.index.dayofweek
for i in range(0,len(hourly_rides_and_weather['day'])):
    if (hourly_rides_and_weather['day'][i])<=4:
        hourly_rides_and_weather['workday'][i]='True'
hourly_rides_and_weather=hourly_rides_and_weather.drop(columns=['day'])
hourly_rides_and_weather['temp']=weather_data.groupby(weather_data.index.floor('D'))['Temp (°C)'].max()
hourly_rides_and_weather['weather']=weather_data.groupby(weather_data.index.floor('D'))['Weather'].count()/24
hourly_rides_and_weather['w']='False'
for i in range(0,len(hourly_rides_and_weather['weather'])):
    if (hourly_rides_and_weather['weather'][i])>0.5:
        hourly_rides_and_weather['w'][i]='Precipitation'
    else:
        hourly_rides_and_weather['w'][i]='clear'
hourly_rides_and_weather=hourly_rides_and_weather.drop(columns=['weather'])
hourly_rides_and_weather=hourly_rides_and_weather.rename(columns={'w':'weather'})

# View DataFrame
hourly_rides_and_weather.head(10)

# investigate the relationship between weather conditions and ridership numbers by using a violin plot
plt.figure(figsize=(10, 5))
sns.violinplot(x=hourly_rides_and_weather['weather'],y=hourly_rides_and_weather['annual_members'])
plt.ylim([0, 15000])
plt.xlabel('Weather Condition')
plt.ylabel("Rides per day")
plt.show()

#investigate the relationship between the maximum daily temperature and ridership numbers
plt.figure(figsize=(10, 5))
sns.scatterplot(x=hourly_rides_and_weather["temp"],y=hourly_rides_and_weather["annual_members"])
sns.scatterplot(x=hourly_rides_and_weather["temp"],y=hourly_rides_and_weather["casual_members"])
plt.legend(labels=["Annual Members","Casual Members"])
plt.xlabel('Maximum Daily Temperature')
plt.ylabel("Rides per day")
plt.title("Effect of Temperature on Daily Rides")
plt.show()

