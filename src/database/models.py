from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class Task(Base):
    __tablename__ = 'tasks'

    text: Mapped[str] = mapped_column()
