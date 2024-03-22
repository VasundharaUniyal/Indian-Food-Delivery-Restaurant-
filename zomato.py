#!/usr/bin/env python
# coding: utf-8

# 1.Import libraries that you required and Load the data set.

# In[73]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[74]:


df = pd.read_csv("Zomoto.CSV")


# In[3]:


df


# 2.Which are the top restaurant chains based on the distribution(frequency) in Bangaluru? 

# In[4]:


casual_dining = df[df['rest_type'] == 'Casual Dining']


# In[5]:


restaurant_counts = df['name'].value_counts()


# In[6]:


top_restaurant_chains = restaurant_counts.head(10)  # Change the number as per your preference
print(top_restaurant_chains)


# 3.How many restaurants do not accept online orders?

# In[13]:


df.rename(columns = {"Unnamed: 0": "rest_id"}, inplace = True)


# In[14]:


df_no = df[df["online_order"]=="No"]
df_no.head()


# In[15]:


nam = df_no['rest_id'].unique()
len(nam)


# In[9]:


nam_lis = df['name'].unique()
len(nam_lis)


# 4.What is the ratio b/w restaurants that provide and do not provide table booking?

# In[17]:


df_bt_yes = df[df['book_table']=="Yes"]

df_bt_no = df[df['book_table']=="No"]

df_bt_yes


# In[18]:


count_bt_yes = len(df_bt_yes['rest_id'].unique())
count_bt_yes

count_bt_no = len(df_bt_no['rest_id'].unique())
count_bt_no

count_total = len(df["rest_id"].unique())
count_total


# In[19]:


ratio_yes = round(count_bt_yes/count_total*100,2)
print(ratio_yes)
ratio_no =  round(count_bt_no/count_total*100,2)
print(ratio_no)


# 5.Use a boxplot on the rating column. Use User Defined Function or Lambda function or Apply function to extract the data that comes before.

# In[100]:


df["rate"].replace(to_replace=["NEW",'-'],value=np.nan,inplace=True)
df.dropna(subset="rate",inplace=True)
r=[]
for i in df["rate"]:
    s=i.split("/")[0]
    r.append(s)
df["rating"]= r


# In[101]:


sns.boxplot(df['rating'])


# In[ ]:





# 6.Online and Offline orders restaurants percentage.

# In[32]:


df_online_no = df[df['online_order']=="No"]
df_online_no


# In[69]:


df_online_yes = df[df['online_order']=="Yes"]
df_online_yes


# In[70]:


count_online_yes = len(df_online_yes['rest_id'].unique())
count_online_yes

count_online_no = len(df_online_no['rest_id'].unique())
count_online_no

count_total


# In[71]:


count_yes =  round(count_online_yes/count_total*100,2)

count_no =  round(count_online_no/count_total*100,2)

print("percentage of rest accepting online order is "+ str(count_yes))
print("percentage of rest not accepting online order is "+ str(count_no))


# 7.Plot the scatter plot using the Cost vs rating variable with respect to online order. Use apply the function Or other function to remove the “,”.

# In[94]:


df.dropna(subset="approx_cost(for two people)",inplace=True)


# In[95]:


def removee(x):
    s=[]
    for i in x:
        
        v=str(i).replace(",",'')
        s.append(int(v))
    return s


# In[96]:


removee(df["approx_cost(for two people)"])
df["approx_cost(for two people)"]=removee(df["approx_cost(for two people)"])


# In[97]:


df['rating']=pd.to_numeric(df['rating'])


# In[99]:


plt.figure(figsize=(15,10))
sns.scatterplot(data=df,y='rating',x="approx_cost(for two people)")


# In[ ]:





# 8.Find the distribution of the votes and Approx_cost using a user-defined function and for a loop.

# In[104]:


def calculate_distribution(data):
    unique_values = np.unique(data)
    distribution = []
    for value in unique_values:
        count = np.count_nonzero(data == value)
        distribution.append((value, count))
    return distribution


# In[110]:


df.groupby(by="approx_cost(for two people)")


# In[113]:


votes_distribution = calculate_distribution(df['votes'])
Approx_cost_distribution = calculate_distribution('Approx cost')


# In[116]:


print("Votes Distribution:")
for value, count in votes_distribution:
    print(f"Value: {value}, Count: {count}")

print("\nApprox Cost Distribution:")
for value, count in Approx_cost_distribution:
    print(f"Value: {value}, Count: {count}")


# In[ ]:





# 9.Which are the most common restaurant type in Banglore?

# In[38]:


df_unique = df.drop_duplicates(subset=["rest_type","rest_id"], keep="first")
df_unique


# In[39]:


df_type_count = df.groupby(['rest_type']).count()
## reset index when row index needs to be converted into column
df_type_count.reset_index(inplace=True)

df_type_count_2 = df_type_count[["rest_type", "rest_id"]]
df_type_count_2


# In[40]:


df_type_count.columns


# In[41]:


df_type_count.columns


# In[42]:


df_type_count_2.sort_values(by=['rest_id'], ascending=False)


# In[43]:


df_type_count_2["rest_id"].max()


# 10.Is there any difference b/w the votes of restaurants accepting and not accepting online orders?

# In[44]:


df_online_no = df[df['online_order']=="No"]
df_online_no


# In[45]:


df_online_yes = df[df['online_order']=="Yes"]
df_online_yes


# In[46]:


df_online_yes['votes'].sum()


# In[47]:


df_online_no['votes'].sum()


# In[48]:


count_votes_yes = df_online_yes['votes'].sum()
count_votes_yes
count_votes_no = df_online_no['votes'].sum()
count_votes_no


# In[50]:


# count_votes = len(df["votes"].unique())
# count_votes


# In[49]:


sub = count_votes_yes - count_votes_no
sub


# 
# 11.	Find the Best budget Restaurants in any location.
# 
# 
# 

# In[51]:


df_budget = df[["name", "approx_cost(for two people)"]]
df_budget


# In[52]:


import numpy as np
# df_budget['budget'] = df_budget['approx_cost(for two people)'].replace(0,np.nan)
df_budget['budget'] = df_budget['approx_cost(for two people)'].fillna(0)

# for whole dataframe
# df = df.replace("NaN", 0)


# In[53]:


df_budget['budget'] = df_budget['budget'].astype(str)


# In[54]:


val = '1,000'
## convert val to int
val.replace("," ,"")
val_int = int(val.replace("," ,""))
type(val_int)

def comma_replacer(val):
    val_int = val.replace("," ,"")
    val_int = int(val_int)

    return val_int


# In[55]:


comma_replacer(df_budget['budget'][9995])


# In[56]:


# df['budget_int']= df_budget['budget'].apply(lambda x: x.replace(',',''))
df_budget['budget_int'] = df_budget['budget'].apply(comma_replacer)
# df.apply(lambda x: addOne(x.A), axis=1)


# In[57]:


df_budget_new = df_budget[df_budget['budget_int']!=0]
df_budget_new = df_budget_new.drop_duplicates()


# In[58]:


df_budget_new.sort_values(by=['budget_int'], ascending=True)


# In[59]:


df_budget


# In[60]:


val = 1000
type(val)


# In[61]:


val = '1,000'


# In[62]:


type(val)


# In[63]:


val = '1,000'
## convert val to int
val.replace("," ,"")
val_int = int(val.replace("," ,""))
type(val_int)


# 12.	Top quick bites restaurant chains in Banglore. *Groupby rest_type, rating , sorting,*duplicated
# 

# In[87]:


x2=df['rest_type'].unique()
x2
x1=df[df['rest_type']=="Quick Bites"]

x2=x1.sort_values(by="rate",ascending=False)
x3=pd.DataFrame(x2['name'].unique())
x3.head(5)


# In[ ]:





# 13.	Which are the most popular casual dining restaurant chains, Make use of any plot related to this question? 

# In[88]:


x= df[df['rest_type']=='Casual Dining']['name'].value_counts().to_frame().head(10)
x


# In[102]:


plt.figure(figsize=(15, 10))
popular_chains.plot(kind='bar')
plt.xlabel('Restaurant Chain')
plt.ylabel('Count')
plt.title('Top 10 Popular Casual Dining Restaurant Chains')
plt.show()


# In[ ]:





# 14.	Which are the most popular cuisines of Bangalore using a related plot?

# In[84]:


plt.pie(df['cuisines'].value_counts(normalize=True).head(),autopct="%.2f%%")
plt.show()


# In[ ]:




