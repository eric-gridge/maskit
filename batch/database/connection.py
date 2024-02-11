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
    from batch.database.table.performance import Performance
    from batch.database.table.performance_price import PerformancePrice
    from batch.database.table.performance_datetime import PerformanceDatetime
    from batch.database.table.performance_person import PerformancePerson

    from batch.database.table import Base

    Base.metadata.create_all(engine)

    print("create tables")