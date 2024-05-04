from sqlalchemy.orm import relationship, mapped_column, Mapped


from app.infrastructure.models.base import Base


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'public'}
    email: Mapped[str] = mapped_column(unique=True, nullable=False, comment='Почта пользователя')
    password: Mapped[str] = mapped_column(nullable=False, comment='Хешированный пароль пользователя')