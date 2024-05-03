from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from ..database.requests import add_task, get_tasks

router = Router()


@router.message(Command('add'))
async def cmd_add_task(message: Message):
    text = message.text.replace('/add', '').strip()

    if text == '':
        await message.answer('Can`t add empty task')
        return

    await add_task(text)
    await message.answer(f'Added new task with text "{text}"')


@router.message(Command('tsk'))
async def cmd_get_tasks(message: Message):
    tasks = await get_tasks()

    if not tasks:
        await message.answer('No tasks')
        return

    for i, task in enumerate(tasks):
        await message.answer(f'{i + 1}. {task.text}')
