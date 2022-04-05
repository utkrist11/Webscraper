#!/usr/bin/env python
# coding: utf-8

# In[11]:


from bs4 import BeautifulSoup
import requests

def main(URL):
	# op file append mode
	File = open("D:/datas/Desktop/please.xml", "a")

	# specifying user agent
	HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

	# HTTP Request
	webpage = requests.get(URL, headers=HEADERS)

	# Creating the Soup Object containing all data
	soup = BeautifulSoup(webpage.content, "lxml")

	# product title
	try:
		# Outer Tag Object
		title = soup.find(
				"span", attrs={'class': 'productTitle fullWidth'})
		title_value = title.string

		# Title as a string value
		title_string = title_value.strip().replace(',', '')

	except AttributeError:
		title_string = "NA"
	print("product Title = ", title_string)

	# savingtitle in file
	File.write(f"{title_string},")

	# retrieving price
	try:
		price =  soup.find(
				"span", attrs={'class': 'AH_PricePerPiece'}).string.strip().replace(',', '')
	except AttributeError:
		price = "NA"
	print("Products price = ", price)

	# saving
	File.write(f"{price},")
    
    
    
	try:
		discount =  soup.find("span", attrs={'id': 'AH_Discount'}).string.strip().replace(',', '')
	except AttributeError:
		discount = "NA"
	print("Products discount = ", discount)

	# saving
	File.write(f"{discount},")

	# retrieving product description
	try:
		description = soup.find("div", attrs={'id': 'description'})
		description = description.find("p", attrs={'class': 'mart'}).string.strip().replace(',', '')
	except AttributeError:

		try:
			description = soup.find("p", attrs={'class': 'mart'}).find_all('p').string.strip().replace(',', '')
		except:
			description = "NA"
	print("Description = ", description)

	File.write(f"{description},")
    
    
	#rating
	try:
		ratings = soup.find("div", attrs={'class': 'pro-review-star'})
		ratings = ratings.find("p").string.strip().replace(',', '')


	except AttributeError:
		ratings = "NA"
	print("Ratings = ", ratings)
	File.write(f"{ratings},")

	# print featurename status

	feature1 = soup.find_all("div", attrs={'class': 'featureNamePr'})
	for ftr in feature1:
		abc = ftr.find(class_="featureNamePr")
		xyz = ftr.text.replace(' ','').replace('\n','')
		File.write(f"{xyz}")
		        
		print("featureName = ", xyz)





    
    
    

    #featureslist
	divTag = soup.find_all("div", attrs={'class': 'featureValuePr'})       
	for tag in divTag:
		unwanted = tag.find('span')
		v = unwanted.extract()
		value1 = tag.text.replace('  ','').replace('\n','')
		File.write(f"{value1},\n")
		print("featuresofproduct = ", value1)


	# saving  and closing the line
	#File.write(f"{value1},\n")

	# closing the file
	File.close()


if __name__ == '__main__': 
    file = open("D:/datas/Desktop/url1.txt", "r")

	# iterating over the urls
    for links in file.readlines():
        main(links)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




