#!/usr/bin/env python
# coding: utf-8

# In[1]:


### HelloFresh Python Assessment ###
# By Jelle Stoffels
# 7 July 2020, Amsterdam

import pandas as pd
import numpy as np
import datetime
import os
import re


# In[2]:


def read(path):
    try:
        recipes = pd.read_json(path, lines=True)
        print('Imported recipes')
        return recipes
    except:
        print('No such file in current directory')
        return None

recipes = read("recipes.json")


# In[3]:


def extract_chilies(df):
    # returns recipes with chilies and saves csv
    chilies = pd.DataFrame([recipe for index, recipe in df.iterrows() 
               if (re.findall(r'\bchill?ie?s?\b', (recipe.ingredients).lower()))])
    
    # add difficulty
    for index, row in chilies.iterrows():
        
        try:   
            Time = (int(re.findall(r'\d+M',row.prepTime)[0][:-1]) + 
                    int(re.findall(r'\d+M',row.cookTime)[0][:-1]))     
        except:
            Time = 61
            
        if Time > 60:
            chilies.at[index, 'difficulty'] = 'Hard'
        elif Time > 30:
            chilies.at[index, 'difficulty'] = 'Medium'
        elif Time > 0:
            chilies.at[index, 'difficulty'] = 'Easy'
        else:
            chilies.at[index, 'difficulty'] = 'Unkown'
    
    chilies.to_csv('chilies_recipes.csv')
    
    return chilies

extract_chilies(recipes).head()


# In[ ]:




