from sqlalchemy import String, BigInteger, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class KeyEvent(Base):
    __tablename__ = "key_events"

    id: Mapped[int] = mapped_column(primary_key=True)
    uid: Mapped[str] = mapped_column(String(32))
    panel_id: Mapped[str] = mapped_column(String(64))
    old_counter: Mapped[int] = mapped_column(BigInteger)
    new_counter: Mapped[int] = mapped_column(BigInteger)
    raw_message: Mapped[str] = mapped_column(Text)
