import os

from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncAttrs
)

load_dotenv()
engine = create_async_engine(url=os.getenv('SQL_URL'))
AsyncSession = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    """
    The base class for all database models.

    Attributes:
        id (Mapped[int]): The primary key of the model.
    """
    id: Mapped[int] = mapped_column(primary_key=True)


async def create_all():
    """
    Create all database tables based
    on the models defined using the `Base` class.

    This function uses an asynchronous context manager
    to ensure that the database connection is properly closed.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
