#!/usr/bin/env python
# coding: utf-8

# In[201]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[221]:


movies = pd.read_csv('http://bit.ly/imdbratings')


# In[4]:


movies.shape


# In[5]:


# knowing the mean and standard deviation of the int columns
movies.describe()


# In[6]:


movies.head()


# In[25]:


# how many movies have duration of 200 and more

lengthy = movies[movies['duration'] >= 200]


# In[98]:


lengthy[['title', 'genre']].count()


# In[30]:


# grouping the movies by genre and sorting it by star rating

movies.groupby('genre').head().sort_values('star_rating')


# In[38]:


# count of movies whose star rating is below 8.0

movies[movies['star_rating'] < 8.0].count()


# In[59]:


# deleting actors_list column 
del movies['actors_list']


# In[ ]:


# I reloaded the url to bring back the deleted column


# In[89]:


# fetching thriller movies with the maximum duration of time

movies[movies['genre'] == 'Thriller'].duration.max()


# In[93]:


movies[movies['genre'] == 'Thriller']


# In[94]:


movies.sort_values('duration')


# In[74]:


movies.columns


# In[95]:


movies.isnull().sum()


# In[137]:


# filtering out not rated movies with at least 8.0 star rating

movies[(movies['content_rating'] == 'NOT RATED') & (movies['star_rating'] >= 8.0)].sort_values('genre').head(4)


# In[136]:


movies[(movies['content_rating'] == 'NOT RATED') & (movies['star_rating'] >= 8.0)][['genre', 'duration']].head(5)


# In[142]:


# changing the columns to a proper case
movies.columns =[x.title() for x in movies.columns]


# In[143]:


movies.head()


# In[178]:


# fetching movies in which Morgan Freeman featured
   
mov_Freeman = movies['Actors_List'].str.contains('Morgan Freeman', na = False)


# In[181]:


movies.loc[mov_Freeman, 'Star_Rating':'Actors_List']


# In[189]:


# movie titles featuring Morgan Freeman

movies.loc[mov_Freeman, ['Title', 'Actors_List']]


# In[ ]:





# In[191]:


# knowing the distribution of movies by genre

movies.groupby('Genre').describe()


# In[199]:


# narrowing down the result given by describe function
movies.groupby('Genre').agg({'Duration': ['max', 'min'],   'Star_Rating': 'min' })


# In[206]:


# transposing the result for better visualization
movies.groupby('Genre').agg({'Duration': ['max', 'min'],   'Star_Rating': 'min' }).T


# In[207]:


# fetching results for Action movie

movies.groupby('Genre').agg({'Duration': ['max', 'min'],   'Star_Rating': 'min' }).loc['Action']


# In[216]:


movies.dtypes


# In[218]:


# setting genre as the index
movies.set_index('Genre', inplace = False)


# In[ ]:




