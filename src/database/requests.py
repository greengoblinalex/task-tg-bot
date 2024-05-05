from sqlalchemy import select

from . import AsyncSession
from .models import Task


async def add_task(text: str) -> None:
    """
    Add a new task to the database.

    Args:
        text (str): The text of the task to be added.
    """
    async with AsyncSession() as session:
        task = Task(text=text)
        session.add(task)
        await session.commit()


async def get_tasks() -> list[Task]:
    """
    Get all tasks from the database.

    Returns:
        list[Task]: A list of all tasks in the database.
    """
    async with AsyncSession() as session:
        result = await session.execute(select(Task))
        tasks = result.scalars().all()
        return tasks
