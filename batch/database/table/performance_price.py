from datetime import datetime
from sqlalchemy import func, insert, String, INT, BIGINT
from sqlalchemy.orm import mapped_column, Mapped

from common.database.connection import db_session_scope
from common.database.table import Base
from common.parse_util import parse_price


class PerformancePrice(Base):
    """
    add index to price column for fast search
    """
    __tablename__ = "performance_price"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    performance_id: Mapped[str] = mapped_column(String(20), index=True, nullable=False)  # mt20id, 공연ID, PF132236
    price: Mapped[int] = mapped_column(INT, index=True, nullable=False)  # pcseguidance, 티켓가격, 전석 30,000 원
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)


def insert_prices(performance_detail):
    prices = performance_detail.get("pcseguidance", "0")
    prices = prices.split("\n")
    objs = [dict(performance_id=performance_detail["mt20id"], price=parse_price(price)) for price in prices]
    with db_session_scope() as session:
        session.execute(insert(PerformancePrice), objs)
