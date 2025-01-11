from sqlalchemy.orm import Session

from ip_networks.database.engine import engine
from ip_networks.database.models import AsInfo, Network


class NetworkPipeline:
    def open_spider(self, spider):
        self.as_info = AsInfo(jobid=spider.jobid, name='', provider='')

    def process_item(self, item, spider):
        network = Network(**item)
        self.as_info.networks.append(network)
        return item

    def close_spider(self, spider):
        self.as_info.name = spider.station
        self.as_info.provider = spider.provider
        with Session(engine) as session:
            session.add(self.as_info)
            session.commit()
