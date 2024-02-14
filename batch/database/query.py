from datetime import datetime

from batch.database.connection import db_session_scope
from batch.database.parse_util import parse_story, parse_time, parse_date_detail, remove_dot, parse_age, \
    parse_datetimes, parse_area, parse_price, parse_names, parse_chosung, parse_enterprise
from batch.database.table import PerformanceItem, PerformanceDatetime, PerformancePrice, PerformancePerson, \
    PerformanceFaculty


def insert_performance(performance_detail: dict, faculty_detail: dict) -> PerformanceItem:
    with db_session_scope() as session:
        item = PerformanceItem(
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
            area=parse_area(performance_detail.get("area", "")),
            daehakro=performance_detail.get("daehakro", "N"),  # default N
            genre=performance_detail.get("genrenm", ""),
            state=performance_detail.get("prfstate", ""),
            price=performance_detail.get("pcseguidance", ""),
            crew=performance_detail.get("prfcrew",""),
            cast=performance_detail.get("prfcast",""),
            story=parse_story(performance_detail.get("sty", "")),
            # enterprise
            host=parse_enterprise(performance_detail.get("entrpsnmH", ""), performance_detail.get("entrpsnmS", "")),
            plan=parse_enterprise(performance_detail.get("entrpsnmP", ""), performance_detail.get("entrpsnmA", "")),
            # from faculty detail
            seats=int(faculty_detail.get("seatscale", 0)),
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        session.add(item)
        session.commit()

        datetimes_original = parse_datetimes(performance_detail.get("dtguidance", ""))
        datetimes = []
        for dt in datetimes_original:
            obj = dict(
                performance_id=item.id,
                day=dt[0],
                time=dt[1],
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            datetimes.append(obj)
        if len(datetimes) > 0:
            session.bulk_insert_mappings(PerformanceDatetime, datetimes)

        people = []
        cast = performance_detail.get("prfcast", "")
        cast_names = parse_names(cast)
        for name in cast_names:
            people.append(dict(performance_id=item.id, name=name, chosung=parse_chosung(name), type="crew",
                               created_at=datetime.now(), updated_at=datetime.now(),))

        crew = performance_detail.get("prfcrew", "")
        crew_names = parse_names(crew)
        for name in crew_names:
            people.append(dict(performance_id=item.id, name=name, chosung=parse_chosung(name), type="cast",
                               created_at=datetime.now(), updated_at=datetime.now(),))

        if len(people) > 0:
            session.bulk_insert_mappings(PerformancePerson, people)

        prices = performance_detail.get("pcseguidance", "0")
        prices = prices.split(", ")
        prices = [dict(performance_id=item.id, price=parse_price(price),
                       created_at=datetime.now(), updated_at=datetime.now(),) for price in prices]

        if len(prices) > 0:
            session.bulk_insert_mappings(PerformancePrice, prices)


def insert_faculty(faculty, faculty_detail):
    with db_session_scope() as session:
        session.add(PerformanceFaculty(
            faculty_id=faculty["mt10id"],
            faculty_name = faculty["fcltynm"],
            area = faculty["sidonm"],
            seatscale = int(faculty_detail.get("seatscale", 0)),
            address = faculty_detail.get("adres", ""),
            created_at = datetime.now(),
            updated_at = datetime.now(),
        ))
