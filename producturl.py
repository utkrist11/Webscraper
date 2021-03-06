#!/usr/bin/env python
# coding: utf-8

# In[2]:



import requests
from bs4 import BeautifulSoup

# url
URL = 'https://www.industrybuying.com/power-tools-641/demolition-hammers-892/'

# request
reqs = requests.get(URL)

# extract all the text 
# the GET request
content = reqs.text

# convert the text to a beautiful soup object
soup = BeautifulSoup(content, 'html.parser')

# Empty list to store the output
urls = []

# For loop that iterates over all the tags
for h in soup.findAll(class_="prFeature"):
	
	# looking for anchor tag inside the tag
	a = h.find(class_="prFeatureName")
	try:
		
		# looking for href inside anchor tag
		if 'href' in a.attrs:
			
			# storing the value of href
			url = a.get('href')
			
			# appending 
			urls.append(url)
			
	
	except:
		pass

# print
for url in urls:
	print('https://www.industrybuying.com/power-tools-641/demolition-hammers-892/'+url)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




