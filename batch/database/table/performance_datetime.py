from datetime import datetime
from sqlalchemy import func, insert, String, INT, BIGINT
from sqlalchemy.orm import mapped_column, Mapped

from batch.database.connection import db_session_scope
from batch.database.table import Base
from batch.parse_util import parse_datetimes


class PerformanceDatetime(Base):
    """
    add index to day, time column for fast search
    """
    __tablename__ = "performance_datetime"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    performance_id: Mapped[str] = mapped_column(String(20), index=True, nullable=False)  # mt20id, 공연ID, PF132236
    day: Mapped[str] = mapped_column(String(20), index=True, nullable=False)  # dtguidance, 공연시간, 화요일 ~ 금요일(20:00), 토요일(15:00,17:30,20:00), 일요일(15:30,18:00) -> parse_datetimes()
    time: Mapped[str] = mapped_column(String(20), index=True, nullable=False)  # dtguidance, 공연시간, 화요일 ~ 금요일(20:00), 토요일(15:00,17:30,20:00), 일요일(15:30,18:00) -> parse_datetimes()
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)


def insert_datetime(performance_detail):
    datetimes = parse_datetimes(performance_detail.get("dtguidance", ""))

    objs = []
    for dt in datetimes:
        obj = dict(
            performance_id=performance_detail["mt20id"],
            day = dt[0],
            time = dt[1]
        )
        objs.append(obj)

    with db_session_scope() as session:
        session.execute(insert(PerformanceDatetime), objs)
