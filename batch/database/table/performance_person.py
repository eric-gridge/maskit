from datetime import datetime
from sqlalchemy import func, insert, String, INT, BIGINT
from sqlalchemy.orm import mapped_column, Mapped

from batch.database.connection import db_session_scope
from batch.database.table import Base


class PerformancePerson(Base):
    """
    add index to name, type column for fast search
    """
    __tablename__ = "performance_person"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    performance_id: Mapped[str] = mapped_column(String(20), index=True, nullable=False)  # mt20id, 공연ID, PF132236
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)  # prfcast(공연출연진), prfcrew(공연제작진), 김부연, 임정균, 최수영
    type: Mapped[str] = mapped_column(String(20), index=True, nullable=False)  # cast or crew
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)


def insert_people(performance_detail):
    objs = []
    cast = performance_detail.get("prfcast", "")
    if cast.endswith(" 등"):
        cast = cast[:-2]
    cast = cast.split(", ")
    for name in cast:
        if name == "" or name == " ":
            continue
        else:
            objs.append(dict(performance_id=performance_detail["mt20id"], name=name, type="cast"))
    crew = performance_detail.get("prfcrew", "")
    if crew.endswith(" 등"):
        crew = crew[:-2]
    crew = crew.split(", ")
    for name in crew:
        if name == "" or name == " ":
            continue
        else:
            objs.append(dict(performance_id=performance_detail["mt20id"], name=name, type="crew"))

    if len(objs) > 0:
        with db_session_scope() as session:
            session.execute(insert(PerformancePerson), objs)
