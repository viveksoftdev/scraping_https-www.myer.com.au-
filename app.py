# import requests
from bs4 import BeautifulSoup
from fetch_pages import main
import aiofiles
import asyncio
import csv
from parse_info import parse_content


list_options = {'men':'all-men','women':'all-women',
                'beauty':'all-beauty','home':'all-home'
                ,'travel-tech':'all-tavel-tech','kids':'all-kids',
                'toys':'all-toys','gifts':'all-gifts','sale':'all-sale',
                'clearance':'all-clearance'}


url_list = [f'https://www.myer.com.au/c/{k}/{list_options.get(k)}'for k in list_options] 




page_num = 180

k = 1
current_url_list = []
for  url in url_list:
    while k <= page_num:
       
        current_url_list.append(url+f'?pageNumber={k}')

        k += 1
    k = 0

root_url = 'https://www.myer.com.au'

product_detail_links = []
#writing urls to a csv product_detail.csv

    


page_content_list = asyncio.run(main(current_url_list)) #page content containing information on many products.

#for each product separate requests would be sent
for content in page_content_list:
    for item in parse_content(content,'div','data-automation','product-detail'):
        product_detail_links.append(root_url+item.select_one('a').get('href')) #link of each product detail page

print(product_detail_links)


file_name = 'product_links'

#writing to csv
import pandas as pd


url_df = pd.DataFrame(product_detail_links)
print(url_df)

url_df.to_csv(file_name,encoding='utf-8-sig')



