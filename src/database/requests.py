from sqlalchemy import select

from . import AsyncSession
from .models import Task


async def add_task(text):
    async with AsyncSession() as session:
        task = Task(text=text)
        session.add(task)
        await session.commit()


async def get_tasks():
    async with AsyncSession() as session:
        result = await session.execute(select(Task))
        tasks = result.scalars().all()
        return tasks
