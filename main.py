import pandas as pd
import asyncio
import pandas as pd
from fetch_pages import main
from parse_info import parse_content
from bs4 import BeautifulSoup


file = 'product_links.csv'


links = pd.read_csv(file)

url_list = links['0'][:3000]

content_list = asyncio.run(main(url_list))

single_product_info = []

file_name = 'product_complete_info.csv'



#['props']
#['dehydratedState']
#['queries']
import json
for content in content_list:
    try:
        soup = BeautifulSoup(content,'html.parser')
        for data in soup.find_all('script')[-1]:
            product_info_list = json.loads(data).get('props').get('pageProps').get('dehydratedState').get('queries')

            for item_dict in product_info_list[3:4]:
           
                api_access = item_dict.get('state').get('data')
                print(api_access.keys())
                data_dict = {'brand_name':api_access.get('brand'),
                         'name':api_access.get('name'),
                         'categoryUri':api_access.get('categoryUri'),
                         'isAvailable':api_access.get('isAvailable'),
                         'promotionEndDate':api_access.get('promotionEndDate'),
                         'priceFrom':api_access.get('priceFrom'),
                         'priceTo':api_access.get('priceTo'),
                         'listPriceFrom':api_access.get('listPriceFrom'),
                         'listPriceTo':api_access.get('listPriceTo'),
                         'savedAmountFrom':api_access.get('savedAmountFrom'),
                         'savedAmountTo':api_access.get('savedAmountTo'),
                         }
                variants = []
            
                for i  in api_access.get('variants'):
                    variant_dict = {'size':i.get('size'),'color':i.get('color'),
                                'listPrice':i.get('listPrice'),
                                'discount':i.get('savedAmount'),'price':i.get('price'),
                                'isStorePickupAllowed':i.get('isStorePickupAllowed'),
                                'itemType':i.get('itemType'),}
                    variants.append(variant_dict)
                data_dict['variants'] = variants

                single_product_info.append(data_dict)
    except Exception as error:
        continue
        
df = pd.DataFrame(single_product_info)
print(df)
df.to_csv(file_name)

  