from sqlalchemy import String, Integer, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class AccessKey(Base):
    __tablename__ = "access_keys"

    id: Mapped[int] = mapped_column(primary_key=True)
    uid: Mapped[str] = mapped_column(String(32))
    panel_id: Mapped[str] = mapped_column(String(64))
    last_counter: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    status: Mapped[str] = mapped_column(String(16), default="ACTIVE")
    suspicion_count: Mapped[int] = mapped_column(Integer, default=0)
