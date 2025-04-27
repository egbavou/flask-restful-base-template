from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from config import Config
# from sqlalchemy.ext.asyncio import create_async_engine

db = SQLAlchemy()

# Create session factories for master and slave databases
SessionMaster = sessionmaker(
    bind = create_engine(
        Config.SQLALCHEMY_DATABASE_WRITE,
        pool_size=10,
        max_overflow=0,
        isolation_level="READ UNCOMMITTED",
        pool_reset_on_return=None,
        pool_pre_ping=True
    ),
    autoflush=False,
    expire_on_commit=False
)
SessionSlave = sessionmaker(
    bind = create_engine(
        Config.SQLALCHEMY_DATABASE_READ,
        pool_size=10, max_overflow=0,
        isolation_level="READ UNCOMMITTED",
        pool_reset_on_return=None,
        pool_pre_ping=True
    ),
    autoflush=False,
    expire_on_commit=False
)

# Create scoped session objects for thread safety
db_session_master = scoped_session(SessionMaster)
db_session_slave = scoped_session(SessionSlave)