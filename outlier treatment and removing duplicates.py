#!/usr/bin/env python
# coding: utf-8

# In[ ]:


trips_data.describe()
trips_data = trips_data.drop(trips_data[trips_data['trip_duration_seconds'] < 60].index)
Q1=trips_data['trip_duration_seconds'].quantile(0.25)
Q3=trips_data['trip_duration_seconds'].quantile(0.75)
IQR = Q3-Q1
trips_data = trips_data.drop(trips_data[trips_data['trip_duration_seconds'] >(Q3+(1.5*IQR))].index)
trips_data = trips_data.drop(trips_data[trips_data['trip_duration_seconds'] <(Q1-(1.5*IQR))].index)

# View DataFrame
trips_data.head()

sns.distplot(trips_data['trip_duration_seconds']/60)
plt.xlabel('Trip Duration, minutes')
plt.ylabel("Probability Density")
plt.title("Distribution of trip duration")
plt.show()


trips_data = trips_data.drop_duplicates(subset =['trip_id'],keep='first')
trips_data = trips_data.reset_index(drop=True)
# View DataFrame
trips_data.head()

