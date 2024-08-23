import aiohttp
import re
import asyncio



async def fetch_page(url,timeout=10):
    timeout_ =  aiohttp.ClientTimeout(timeout)
    c = 0
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                print(f'getting {url}')
                return await resp.text()
    except asyncio.TimeoutError as error :
        if c == 5:
            print(f'{url} failed')
            return ''
        else:
            c += 1
            print(f'{url} failed')
            await fetch_page(url)
    except Exception as error:
        return ''
        
async def main(url_list,timeout=10):
    return await asyncio.gather(*(fetch_page(url,timeout) for url in url_list))

