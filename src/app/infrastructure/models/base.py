import uuid

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    oid: Mapped[uuid.UUID] = mapped_column(primary_key=True, comment='uuid элемента')
