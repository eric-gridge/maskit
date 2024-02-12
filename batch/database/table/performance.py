from datetime import datetime
from sqlalchemy import func, insert, String, INT, TEXT, BIGINT
from sqlalchemy.orm import mapped_column, Mapped

from batch.database.connection import db_session_scope
from batch.database.table import Base
from batch.parse_util import remove_dot, parse_age, parse_story, parse_date_detail, parse_time


class Performance(Base):
    __tablename__ = "performance"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    performance_id: Mapped[str] = mapped_column(String(20), index=True, nullable=False)  # mt20id, 공연ID, PF132236
    name: Mapped[str] = mapped_column(String(255), nullable=False)  # prfnm, 공연명, 우리연애할까
    faculty_id: Mapped[str] = mapped_column(String(20), nullable=False)  # mt10id, 공연시설ID,
    faculty_name: Mapped[str] = mapped_column(String(255), nullable=False)  # fcltynm, 공연시설명(공연장명), 피가로아트홀(구 훈아트홀)
    age: Mapped[int] = mapped_column(INT, nullable=False)  # prfage, 나이 - for search
    age_detail: Mapped[str] = mapped_column(String(255), nullable=False)# prfage, 나이 - for view
    date_from: Mapped[str] = mapped_column(String(20), nullable=False)  # prfpdfrom, 공연시작일, 2016.05.12 -> remove_dot() - for search
    date_to: Mapped[str] = mapped_column(String(20), nullable=False)  # prfpdto, 공연종료일, 2016.07.31 -> remove_dot() - for search
    date_detail: Mapped[str] = mapped_column(String(255), nullable=False)  # prfpdfrom, prfpdto - for view
    time: Mapped[str] = mapped_column(TEXT, nullable=False)  # dtguidance, 공연시간, 화요일 ~ 금요일(20:00), 토요일(15:00,17:30,20:00), 일요일(15:30,18:00)
    poster: Mapped[str] = mapped_column(String(255), nullable=False)  # poster, 포스터이미지경로, http://www.kopis.or.kr/upload/pfmPoster/PF_PF132236_160704_142630.gif
    area: Mapped[str] = mapped_column(String(255), nullable=False)  # area, 공연지역, 서울특별시
    genre: Mapped[str] = mapped_column(String(255), nullable=False)  # genrenm, 공연 장르명, 연극
    state: Mapped[str] = mapped_column(String(20), nullable=False)  # prfstate, 공연상태, (공연중)
    price: Mapped[str] = mapped_column(String(255), nullable=False)
    crew: Mapped[str] = mapped_column(String(255), nullable=False)
    cast: Mapped[str] = mapped_column(String(255), nullable=False)
    story: Mapped[str] = mapped_column(TEXT, nullable=False)  # sty, 줄거리
    enterprise_p: Mapped[str] = mapped_column(String(255), nullable=False)  # entrpsnmP(제작사)
    enterprise_a: Mapped[str] = mapped_column(String(255), nullable=False)  # entrpsnmA(기획사)
    enterprise_h: Mapped[str] = mapped_column(String(255), nullable=False)  # entrpsnmH(주최)
    enterprise_s: Mapped[str] = mapped_column(String(255), nullable=False)  # entrpsnmS(주관)
    seats: Mapped[int] = mapped_column(INT, nullable=False)  # seatscale, 객석 수, 32349
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)


def insert_performance(performance_detail, faculty_detail):
    obj = dict(
        performance_id=performance_detail["mt20id"],
        name=performance_detail["prfnm"],
        faculty_id=performance_detail["mt10id"],
        faculty_name=performance_detail["fcltynm"],
        # parse age
        age=parse_age(performance_detail.get("prfage", "")),
        age_detail=performance_detail.get("prfage", ""),
        # remove dot from date
        date_from=remove_dot(performance_detail.get("prfpdfrom", "")),
        date_to=remove_dot(performance_detail.get("prfpdto", "")),
        date_detail=parse_date_detail(performance_detail.get("prfpdfrom", ""), performance_detail.get("prfpdto", "")),
        # add default value
        time=parse_time(performance_detail.get("dtguidance", "")),
        poster=performance_detail.get("poster", ""),
        area=performance_detail.get("area", ""),
        genre=performance_detail.get("genrenm", ""),
        state=performance_detail.get("prfstate", ""),
        price=performance_detail.get("pcseguidance", ""),
        crew=performance_detail.get("prfcrew",""),
        cast=performance_detail.get("prfcast",""),
        story=parse_story(performance_detail.get("sty", "")),
        # enterprise
        enterprise_p=performance_detail.get("entrpsnmP", ""),
        enterprise_a=performance_detail.get("entrpsnmA", ""),
        enterprise_h=performance_detail.get("entrpsnmH", ""),
        enterprise_s=performance_detail.get("entrpsnmS", ""),
        # from faculty detail
        seats=int(faculty_detail.get("seatscale", 0))
    )

    with db_session_scope() as session:
        session.execute(insert(Performance), [obj])
