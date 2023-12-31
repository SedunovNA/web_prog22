
    # accountr/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .settings import settings
engine = create_engine(settings.database_url,
connect_args={'check_same_thread': False}, )
Session = sessionmaker(bind=engine,
autocommit=False, autoflush=False,
                           )