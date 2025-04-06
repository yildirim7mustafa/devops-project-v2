from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, Text
from .database import Base
from sqlalchemy.sql import func

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable= False)
    title = Column(String, nullable= False)
    content = Column(String, nullable= False)
    published = Column(Boolean,server_default='TRUE', nullable= False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())  # ✅ Doğru kullanım
