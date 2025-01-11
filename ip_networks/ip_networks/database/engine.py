from sqlalchemy import create_engine

from .models import Base
from ip_networks.settings import db_settings


engine = create_engine(db_settings.database_url, pool_pre_ping=True)

Base.metadata.create_all(engine)
