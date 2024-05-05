from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class Task(Base):
    """
    Represents a task in the database.

    Attributes:
        text (Mapped[str]): The text of the task.
    """
    __tablename__ = 'tasks'

    text: Mapped[str] = mapped_column()
