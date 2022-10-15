import asyncio
import httpx
import time


class AsyncService:
    async def main(self, articles_list):
        result = list()
        start_time = time.time()
        result.append(
            await asyncio.gather(*(self.data_by_articles(article) for article in articles_list))
        )
        print("--- %s seconds ---" % (time.time() - start_time))
        return result[0]

    async def data_by_articles(self, article):
        data = dict()

        async with httpx.AsyncClient() as client:
            request = await client.get(f'https://card.wb.ru/cards/detail?nm={article}')

        product_data = request.json()['data']['products'][0]
        data['article'] = article
        data['brand'] = product_data['brand']
        data['title'] = product_data['name']
        return data
