from urllib.parse import urlparse

import scrapy

from ip_networks.items import IpNetworksItem

# cd ip_networks/
# scrapy crawl networks
# python parse.py
# 'https://bgp.he.net/AS3326'


IP_V4 = 4
IP_V6 = 6


class NetworksSpider(scrapy.Spider):
    name = 'networks'

    def __init__(self, link, *args, **kwargs):
        super(NetworksSpider, self).__init__(*args, **kwargs)
        self.link = link
        self.jobid = kwargs.get('_job')

    def start_requests(self):
        yield scrapy.Request(url=self.link, callback=self.parse)

    def parse(self, response):
        self.station = urlparse(response.url).path.replace('/', '')
        header = response.css('[id=header] h1 a').attrib['title']
        self.provider = header.split(maxsplit=1)[-1]

        for ip_version in (IP_V4, IP_V6):
            for row in response.css(
                f'[id=table_prefixes{ip_version}] tbody tr'
            ):
                tds = row.css('td')
                yield IpNetworksItem(
                    {
                        'network': tds[0].css('a::text').get(),
                        'provider': tds[1].css('::text').get().strip(),
                        'country': tds[1].css('img').attrib['title'],
                        'ip_version': ip_version
                    }
                )
