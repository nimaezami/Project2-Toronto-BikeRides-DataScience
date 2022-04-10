#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#adding day and weekday_name to hourly_rides_and_weather 
hourly_rides_and_weather['day']= hourly_rides_and_weather.index.dayofweek
hourly_rides_and_weather['weekday_name']= hourly_rides_and_weather.index.day_name()

#group by weekday_name for july 2021
cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hourly_rides_and_weather_2021=hourly_rides_and_weather.loc['2021-07']
day_of_week = pd.DataFrame()
day_of_week['rides']=hourly_rides_and_weather_2021.groupby('weekday_name').rides.sum()
day_of_week['annual_members']=hourly_rides_and_weather_2021.groupby('weekday_name').annual_members.sum()
day_of_week['casual_members']=hourly_rides_and_weather_2021.groupby('weekday_name').casual_members.sum()
day_of_week=day_of_week.reindex(cats) 
day_of_week.head()

#visulasing bike ride trend in july 2021
plt.figure(figsize=(10, 6))
plt.bar(day_of_week.index,day_of_week['rides'],width = 0.25)
plt.bar(day_of_week.index,day_of_week['annual_members'],width = 0.25)
plt.bar(day_of_week.index,day_of_week['casual_members'],width = 0.25)
plt.xlabel('weekday_name')
plt.ylabel("Number of trips based on weekday")
plt.title("Toronto city Bike Rides per day of week on July 2021")
plt.legend(["rides", "annual_members","casual_members"])
plt.show()

