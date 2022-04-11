#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from matplotlib.dates import DateFormatter
from matplotlib.ticker import FuncFormatter
from matplotlib.dates import MonthLocator, DateFormatter 

#Monthly rides dataframe
data_month = pd.DataFrame()
data_month['rides']=trips_data.groupby('trip_start_time').size().resample('m').sum()
data_month['annual_members']=trips_data[trips_data['user_type']=='Annual Member'].groupby('trip_start_time').size().resample('m').sum()
data_month['casual_members']=trips_data[trips_data['user_type']=='Casual Member'].groupby('trip_start_time').size().resample('m').sum()

#visualization of Monthly rides
plt.figure(figsize=(15, 7))
ax = plt.subplot()
ax.bar(data_month.index,data_month['rides']/1000, width=20)
ax.bar(data_month.index,data_month['annual_members']/1000, width=20)
ax.bar(data_month.index,data_month['casual_members']/1000, width=20)
ax.xaxis_date()

month_fmt = DateFormatter('%b')
def m_fmt(x, pos=None):
    return month_fmt(x)[0]

ax.xaxis.set_minor_locator(MonthLocator())
ax.xaxis.set_minor_formatter(FuncFormatter(m_fmt))
ax.set_title('Monthly Bike Share Rides in the city of Toronto for 2017-2022')
ax.set_xlabel('Date-Time')
ax.set_ylabel('Monthly Rides(thousands)')
ax.legend(["rides","annual_members","casual_members"])



# Move the category label further from x-axis
ax.tick_params(axis='x', which='major', pad=15)

plt.show()

