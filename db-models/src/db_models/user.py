from sqlalchemy.orm import Mapped, mapped_column

from db_models.base import Base


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]

    def __repr__(self) -> str:
        return f"{self.name} ({self.age})"
