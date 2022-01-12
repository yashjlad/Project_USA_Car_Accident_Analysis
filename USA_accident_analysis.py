#!/usr/bin/env python
# coding: utf-8

# # US Accidents Exploratory Data Analysis

# ## Data download

# In[4]:


pip install opendatasets --upgrade


# In[5]:


import opendatasets as od 

dataset_url ='https://www.kaggle.com/sobhanmoosavi/us-accidents'

od.download(dataset_url)


# In[7]:


data_filename ='./us-accidents/US_Accidents_Dec20_updated.csv'


# ## Data Preparation and Cleaning

# 1. Loading the file using Pandas
# 2. Have a look at the information about the data and coloumns
# 3. Fix any missing or incorect values 

# In[8]:


import pandas as pd 


# In[9]:


df = pd.read_csv(data_filename)


# In[10]:


df


# In[8]:


df.columns


# In[9]:


len(df.columns)


# In[10]:


df.info()


# In[11]:


df.describe()


# In[12]:


numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

numeric_df = df.select_dtypes(include=numerics)
len(numeric_df.columns)


# ## Find the percentage of missing values in the data 

# In[13]:


missing_percentages = df.isna().sum().sort_values(ascending=False)/len(df)
missing_percentages*100


# In[14]:


pip install matplotlib


# In[38]:


type(missing_percentages)


# In[42]:


missing_percentages[missing_percentages!=0]*100


# In[44]:


missing_percentages[missing_percentages!=0].plot(kind='barh')


# ## Removing missing value columns from the data 

# In[ ]:





#  ## Questions and Answers

# 1. Are there more accidents in warmer or colder areas?
# 2. Which 5 states has the highest number of accidents? Accidents per capita
# 3. Does new York show up in the data? Why does the count is lower if its the most populated city in United States. 
# 4. Among the top 100 cities in the number of accidents, which states do they belong to?
# 5. What time of the day are accidents more frequent?
# 6. Which days of the week have the most accidents?
# 7. Which months of the year have the most accidents?
# 8. What's the trend in the number of accidents per year?

# Coloumns to analyze:
# 1. City
# 2. Start Time
# 3. Start Lat
# 4. Temp
# 5. Weather Condition  

# ### City 

# In[50]:


unique_cities=  df.City.unique()
len(unique_cities)


# In[56]:


cities_by_accident = df.City.value_counts()
cities_by_accident[:20]


# In[60]:


'New York' in df.State


# In[61]:


cities_by_accident[:20].plot(kind='barh')


# In[22]:


import seaborn as sns
sns.set_style("darkgrid")


# In[67]:


sns.distplot(cities_by_accident)


# In[88]:


high_accident_cities =cities_by_accident[cities_by_accident>=1000]
low_accident_cities =cities_by_accident[cities_by_accident<1000]


# In[79]:


len(high_accident_cities)


# In[84]:


len(high_accident_cities)/len(unique_cities)*100


# In[89]:


sns.distplot(high_accident_cities)


# In[90]:


sns.distplot(low_accident_cities)


# In[92]:


sns.histplot(low_accident_cities, log_scale=True)


# In[99]:


cities_by_accident[cities_by_accident==10]


# ### Start time 

# In[3]:


df.Start_Time


# In[103]:


df.Start_Time


#    ### Convert the start time into time stamps

# In[16]:


df.Start_Time= pd.to_datetime(df.Start_Time) 


# In[20]:


df.Start_Time[0]


# ### Extract only hours from the timestamps 

# In[18]:


df.Start_Time.dt.hour


# In[27]:


sns.distplot(df.Start_Time.dt.hour, bins=24, kde=False, norm_hist=True)


# In[29]:


sns.distplot(df.Start_Time.dt.dayofweek, bins=7, kde=False, norm_hist=True)


# ### Is the distibution of accidents by the hour same on weekends as on weekdays?

# In[43]:


Sunday_start_time = df.Start_Time[df.Start_Time.dt.dayofweek==6]
sns.distplot(Sunday_start_time.dt.hour, bins=24, kde=False, norm_hist=True)


# ### On weekends the maximum number of accidents occur between 4-12pm because most people are outside having fun on the weekends. 

# In[47]:


Monday_start_time = df.Start_Time[df.Start_Time.dt.dayofweek==5]
sns.distplot(Monday_start_time.dt.hour, bins=24, kde=False, norm_hist=True)


# ### Whereas while comparing the data for the weekdays most accidents occur between 6 to 9 am and 3 to 6pm 

# In[49]:


sns.distplot(df.Start_Time.dt.month, bins=12, kde=False, norm_hist=True)


# ### Because of the holiday season, the number of vehicles on the road are more than normal which leads to more accidents. 

# In[68]:


df_2019 = df.Start_Time[df.Start_Time.dt.year == 2019]
sns.distplot(df_2019.dt.month, bins=12 , kde=False, norm_hist=True)


# ### Much data is missing for 2016, 2017, 2019

# ## Start Latitude an Longitude
# 

# In[75]:


df.Start_Lat


# In[77]:


df.Start_Lng


# In[79]:


sample_df=df.sample(0.1)
sns.scatterplot(x=df. art_Lng, y=df.Start_Lat)


# In[80]:


import folium


# In[81]:


import folium


# In[90]:


lat, lng = df.Start_Lat[0], df.Start_Lng[0]
lat, lng


# In[104]:


map= folium.Map()
marker = folium.Marker((lat, lon))
marker.add_to(map)
map


# In[108]:


zip(list(df.Start_Lat), list(df.Start_Lng))


# In[112]:


from folium.plugins import HeatMap


# In[117]:


sample_df = df.sample(int(0.1 * len(df)))
lat_lon_pairs = list(zip(list(sample_df.Start_Lat), list(sample_df.Start_Lng)))


# In[118]:


map = folium.Map()
HeatMap(lat_lon_pairs).add_to(map)
map


# ## Summary and Conclusion 

# 1. No data for New York
# 2. Less than 5% of the cities have more than 1000 accidents per year
# 3. There are over 1200 cities have reported just 1 accident. It doesn't makes sense because the data is collected for four years. Needs investigation 
# 4. The number of accidents per city follows a decreasing exponential pattern
# 5. 

# In[ ]:





# In[ ]:




