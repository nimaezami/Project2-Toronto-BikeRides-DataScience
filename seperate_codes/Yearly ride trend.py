#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#create yearly ride dataframe
data_year = pd.DataFrame()
data_year['rides']=trips_data.groupby('trip_start_time').size().resample('Y').sum()
data_year['annual_members']=trips_data[trips_data['user_type']=='Annual Member'].groupby('trip_start_time').size().resample('Y').sum()
data_year['casual_members']=trips_data[trips_data['user_type']=='Casual Member'].groupby('trip_start_time').size().resample('Y').sum()
data_year['year']=data_year.index.year

#visualizing yearly ride dataframe
fig = plt.figure(figsize=(15, 7))
ax = fig.add_axes([0,0,1,1])
ax.bar(data_year['year']+0.00,data_year['rides']/1000, color = 'b', width = 0.25)
ax.bar(data_year['year']+0.25,data_year['annual_members']/1000, color = 'g', width = 0.25)
ax.bar(data_year['year']+0.50,data_year['casual_members']/1000, color = 'r', width = 0.25)
ax.set_title('Yearly Bike Share Rides in the city of Toronto for 2017-2022')
ax.set_xlabel('Date-Time')
ax.set_ylabel('Yearly Rides(thousands)')
ax.legend(["rides","annual_members","casual_members"])
plt.xticks()
plt.show()

