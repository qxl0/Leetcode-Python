from bisect import bisect_left
from collections import Counter
import heapq
from math import inf
from re import I
from typing import List
from concurrent.futures import ThreadPoolExecutor
import asyncio


class Solution:
    async def processUrl(self, url):
        self.seen.add(url)
        urls = set(
            u for u in await self.parse_url_async(url) if u.startswith(self.hostname)
        )
        not_vis = urls - self.seen

        await asyncio.gather(*(self.processUrl(u) for u in not_vis))

    async def parse_url_async(self, url):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            self.executor(self.executor, self.htmlParser.getUrls, url)
        )

    def crawl(self, startUrl, htmlParser):
        self.seen = set()
        self.hostname = "/".join(startUrl.split("/", 3)[:3])
        self.htmlParser = htmlParser

        with ThreadPoolExecutor(max_workers=64) as self.executor:
            asyncio.run(self.process_url(startUrl))

        return self.seen


if __name__ == "__main__":
    sol = Solution()
    startUrl = "http://news.yahoo.com/news/topics/"
    res = sol.crawl(startUrl)
    print(res)
