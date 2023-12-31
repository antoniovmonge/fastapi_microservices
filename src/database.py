from src.config import settings

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class Database:
    def __init__(self):
        self.__session = None
        self.__engine = None

    def connect(self, db_config):
        self.__engine = create_async_engine(
            settings.database_url,
        )

        self.__session = async_sessionmaker(
            bind=self.__engine,
            autocommit=False,
        )

    async def disconnect(self):
        await self.__engine.dispose()

    async def get_db(self):
        async with db.__session() as session:
            yield session


db = Database()
