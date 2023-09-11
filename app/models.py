from datetime import datetime
from sqlalchemy import text, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship, Mapped


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str]
    published: Mapped[bool] = mapped_column(server_default='TRUE')
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=text('now()'))
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    owner: Mapped["User"] = relationship("User")


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=text('now()'))


class Vote(Base):
    __tablename__ = 'votes'

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
