#!/usr/bin/env python
# coding: utf-8

# In[33]:


#dependencies
import os
import time
import requests
import warnings
import pandas as pd
from splinter import Browser
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager


# In[34]:


#the path to the chromedriver
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[35]:


url = "https://mars.nasa.gov/news"
browser.visit(url)
html = browser.html
soup = bs(html, 'lxml')


# In[36]:


first_article = soup.find_all('li', class_='slide')[0]
print(first_article.prettify())


# In[37]:


news = soup.find('li', class_='slide')
print(news)


# In[38]:


news_headline = news.find(class_="content_title").text
print(news_headline)


# In[39]:


new_paragraph = news.find(class_="article_teaser_body").text
print(new_paragraph)


# In[40]:


#Visit JPL url included in the instruction
#https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html
url2= "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
browser.visit(url2)
html = browser.html
soup = bs(html, 'lxml')


# In[41]:


image_url = soup.find_all('div', class_='header')[0]
print(image_url)


# In[42]:


featured_image_sub_url = image_url.find('img', class_='headerimage fade-in')
featured_image_sub_url = featured_image_sub_url.attrs.get('src', None)
print(featured_image_sub_url)


# In[43]:


featured_image_url = os.path.dirname(url2)
print(featured_image_url)


# In[44]:


complete_image_url = f'{url2}/{featured_image_sub_url}'
print(complete_image_url)


# In[45]:


facts_url = "https://space-facts.com/mars/"
tables = pd.read_html(facts_url)
print(tables)


# In[46]:


mars_facts_df = tables[0]
mars_facts_df


# In[47]:


mars_html = mars_facts_df.to_html()
text_file = open("mars_html.html", "w")
text_file.write(mars_html)
text_file.close()


# In[48]:


mars_html


# In[49]:


mars_html = mars_html.replace('\n', '')
mars_html


# In[99]:


image_urls = "https://astrogeology.usgs.gov/search/map/Mars/Viking/"
image_urls


# In[100]:


cerberus_url = (f'{image_urls}cerberus_enhanced')
schiaparelli_url = (f'{image_urls}schiaparelli_enhanced')
syrtis_major_url = (f'{image_urls}syrtis_major_enhanced')
valles_marineris_url = (f'{image_urls}valles_marineris_enhanced')


# In[101]:


print(cerberus_url)
print(schiaparelli_url)
print(syrtis_major_url)
print(valles_marineris_url)


# In[102]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": valles_marineris_url},
    {"title": "Cerberus Hemisphere", "img_url": cerberus_url},
    {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_url},
    {"title": "Syrtis Major Hemisphere", "img_url": syrtis_major_url},
]
print(hemisphere_image_urls)


# In[103]:


#browser.quit()

# In[ ]:




