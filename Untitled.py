#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import xlrd
import matplotlib.pyplot as plt 
import plotly.express as px 
import plotly


# In[2]:


responses=pd.read_excel(r"C:\Users\prach\OneDrive\Desktop\TUM_essay\Responses.xlsx",sheet_name="in")


# In[3]:


responses.head()
responses.drop(columns=['Timestamp'],inplace=True)


# In[4]:


new_column_name=['age','number_social_media','source_news','authenticity_doubt','prompt_forward_message','share_reading_headlines']
present_columns=responses.columns.tolist()
rename_columns={}
for x in range(0,len(present_columns)):
    print(x)
    rename_columns[present_columns[x]]=new_column_name[x]
print(rename_columns)            
responses.rename(columns=rename_columns,inplace=True)


# In[5]:


responses


# #   AGE GROUPS 
# we have 4 different age groups lets see the number of test cases for each of them

# In[6]:


age_df=responses.groupby(['age']).size().reset_index(name='number')
x=age_df['age']
responses.columns
y=age_df['number']
age_df


# In[7]:


my_circle=plt.Circle( (0,0), 0.5, color='white')
plt.pie(y, labels=x,wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' },autopct='%1.0f%%', pctdistance=.7, labeldistance=1.2)
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.savefig(r"C:\Users\prach\OneDrive\Desktop\TUM_essay\age_stats.png",dpi=100,transparent=True,facecolor = 'white')
plt.show()


# ## Social media distribution according to age
# Usage of social media across different age groups

# In[8]:


age_number_social_media=responses.groupby(['age','number_social_media']).size().reset_index(name='frequency')


# In[9]:


fig = px.bar(age_number_social_media, x="age", y="frequency",color_discrete_sequence=px.colors.qualitative.T10,
             color="number_social_media", barmode = 'group')  
fig.show()
plotly.offline.plot(fig, filename=r"C:\Users\prach\OneDrive\Desktop\TUM_essay\age_social_media.html")


# # #News Source
# Meduim of news accross various age groups

# In[10]:


age_news=responses.groupby(['age','source_news']).size().reset_index(name='frequency')
age_news


# In[11]:


fig = px.bar(age_news, x="age", y="frequency",color_discrete_sequence=px.colors.qualitative.T10,
             color="source_news", barmode = 'group')  
fig.show()
plotly.offline.plot(fig, filename=r"C:\Users\prach\OneDrive\Desktop\TUM_essay\news_age_group.html")


# ## Fake News Spread
# Since the majority of the samples belong to the age 20-30 and 30-40 we will be anlyzing fake
# news spread for these two cohorts seperately

# In[12]:


responses_20_30=responses[responses['age']=='20-30'].copy()
responses_30_40=responses[responses['age']=='30-40'].copy()


# #### Fake news spread in 20-30

# In[13]:


authenticity_doubt_20_30=responses_20_30.groupby(['authenticity_doubt']).size().reset_index(name='frequency')
authenticity_doubt_20_30


# In[16]:


x=authenticity_doubt_20_30['authenticity_doubt'].tolist()
y=authenticity_doubt_20_30['frequency'].tolist()
my_circle=plt.Circle( (0,0), 0.5, color='white')
plt.pie(y, labels=x,wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' },autopct='%1.0f%%', pctdistance=.7, labeldistance=1)
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.savefig(r"C:\Users\prach\OneDrive\Desktop\TUM_essay\authenticity_doubt_20_30.png",dpi=100,transparent=True,facecolor = 'white')
plt.show()


# ##### Doubting the authenticity against reason for forwarding information

# In[17]:


authenticity_doubt_forward_prompt_20_30=responses_20_30.groupby(['authenticity_doubt','prompt_forward_message']).size().reset_index(name='frequency')
authenticity_doubt_forward_prompt_20_30


# In[19]:


fig = px.bar(authenticity_doubt_forward_prompt_20_30, x="authenticity_doubt", y="frequency",color_discrete_sequence=px.colors.qualitative.T10,
             color="prompt_forward_message", barmode = 'group')  
fig.show()
plotly.offline.plot(fig, filename=r"C:\Users\prach\OneDrive\Desktop\TUM_essay\authenticity_doubt_forward_prompt_20_30.html")


# ##### Doubting an information against passing on information without reading it in details

# In[20]:


authenticity_doubt_share_reading_heading_20_30=responses_20_30.groupby(['authenticity_doubt','share_reading_headlines']).size().reset_index(name='frequency')
authenticity_doubt_share_reading_heading_20_30


# In[21]:


fig = px.bar(authenticity_doubt_share_reading_heading_20_30, x="authenticity_doubt", y="frequency",color_discrete_sequence=px.colors.qualitative.T10,
             color="share_reading_headlines", barmode = 'group')  
fig.show()
plotly.offline.plot(fig, filename=r"C:\Users\prach\OneDrive\Desktop\TUM_essay\authenticity_doubt_share_reading_heading_20_30.html")


# ### Fake news spread in 30-40

# In[22]:


authenticity_doubt_30_40=responses_30_40.groupby(['authenticity_doubt']).size().reset_index(name='frequency')
authenticity_doubt_30_40


# In[23]:


x=authenticity_doubt_30_40['authenticity_doubt'].tolist()
y=authenticity_doubt_30_40['frequency'].tolist()
my_circle=plt.Circle( (0,0), 0.5, color='white')
plt.pie(y, labels=x,wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' },autopct='%1.0f%%', pctdistance=.7, labeldistance=1)
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.savefig(r"C:\Users\prach\OneDrive\Desktop\TUM_essay\authenticity_doubt_30_40.png",dpi=100,transparent=True,facecolor = 'white')
plt.show()


# ##### Doubting the authenticity against reason for forwarding information

# In[24]:


authenticity_doubt_forward_prompt_30_40=responses_30_40.groupby(['authenticity_doubt','prompt_forward_message']).size().reset_index(name='frequency')
authenticity_doubt_forward_prompt_30_40


# In[25]:


fig = px.bar(authenticity_doubt_forward_prompt_30_40, x="authenticity_doubt", y="frequency",color_discrete_sequence=px.colors.qualitative.T10,
             color="prompt_forward_message", barmode = 'group')  
fig.show()
plotly.offline.plot(fig, filename=r"C:\Users\prach\OneDrive\Desktop\TUM_essay\authenticity_doubt_forward_prompt_30_40.html")


# ##### Doubting an information against passing on information without reading it in details

# In[26]:


authenticity_doubt_share_reading_heading_30_40=responses_30_40.groupby(['authenticity_doubt','share_reading_headlines']).size().reset_index(name='frequency')
authenticity_doubt_share_reading_heading_30_40


# In[27]:


fig = px.bar(authenticity_doubt_share_reading_heading_30_40, x="authenticity_doubt", y="frequency",color_discrete_sequence=px.colors.qualitative.T10,
             color="share_reading_headlines", barmode = 'group')  
fig.show()
plotly.offline.plot(fig, filename=r"C:\Users\prach\OneDrive\Desktop\TUM_essay\authenticity_doubt_share_reading_heading_30_40.html")


# In[ ]:




