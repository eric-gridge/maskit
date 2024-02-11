from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("mysql+pymysql://root:1234@localhost:3306/maskit")


@contextmanager
def db_session_scope():
    with Session(engine) as session:
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e  # raise again after rollback session.
        finally:
            session.close()


if __name__ == "__main__":
    from common.database.table.performance import Performance
    from common.database.table.performance_price import PerformancePrice
    from common.database.table.performance_datetime import PerformanceDatetime
    from common.database.table.performance_person import PerformancePerson

    from common.database.table import Base

    Base.metadata.create_all(engine)

    print("create tables")