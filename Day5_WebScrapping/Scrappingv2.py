# -*- coding: utf-8 -*-
#############################################################
#############################################################
###### Script to scrape PDF documents from a website ########
#############################################################
#############################################################

"""
Created on Thu Oct  7 15:51:07 2021
@author: Alfonso
"""

# Packages
import requests
from bs4 import BeautifulSoup
from urllib.request import unquote

#target URL
url = 'url_address'

### make HTTP GET request to the target URL ###
print('HTTP GET: %s', url)
response = requests.get(url)

# parse content
content = BeautifulSoup(response.text, 'lxml')

# extract URLs referencing PDF documents
all_urls = content.find_all('a')

# loop over all URLs
for url in all_urls:
    # try URLs containing 'href' attribute
    try:
        # pick up only those URLs containing 'pdf'
        # within 'href' attribute
        if 'pdf' in url['href']:
            # init PDF url
            pdf_url = ''
            
            # append base URL if no 'https' available in URL
            if 'https' not in url['href']:
                pdf_url = 'url_address' + url['href']

            # otherwise use bare URL
            else:
                pdf_url = url['href']
            
            # make HTTP GET request to fetch PDF bytes
            print('HTTP GET: %s', pdf_url)          
            pdf_response = requests.get(pdf_url)
            
            # extract  PDF file name
            filename = unquote(pdf_response.url).split('/')[-1].replace(' ', '_')
            
            # write PDF to local file
            with open('./pdf/' + filename, 'wb') as f:
                # write PDF to local file
                f.write(pdf_response.content)
    
    # skip all the other URLs
    except:
        pass
