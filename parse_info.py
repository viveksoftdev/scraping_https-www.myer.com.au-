from bs4 import BeautifulSoup





def parse_content(page_content,tag,attr,attrs_value):
    page = BeautifulSoup(page_content,'html.parser')
  
    selector = f'{tag}[{attr}^="{attrs_value}"]'
    return page.select(selector)

    
