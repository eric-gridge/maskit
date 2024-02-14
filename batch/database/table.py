from sqlalchemy import Column, BigInteger, String, Integer, DATETIME, ForeignKeyConstraint, Index, func
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class PerformanceItem(Base):
    __tablename__ = 'performance_item'

    id = Column(BigInteger, primary_key=True)
    performance_id = Column(String(20), nullable=False)
    name = Column(String(255), nullable=False)
    faculty_id = Column(String(20), nullable=False)
    faculty_name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    age_detail = Column(String(255), nullable=False)
    date_from = Column(String(20), nullable=False)
    date_to = Column(String(20), nullable=False)
    date_detail = Column(String(255), nullable=False)
    time = Column(LONGTEXT, nullable=False)
    poster = Column(String(255), nullable=False)
    area = Column(String(255), nullable=False)
    daehakro = Column(String(2), nullable=False)
    genre = Column(String(255), nullable=False)
    state = Column(String(20), nullable=False)
    price = Column(String(255), nullable=False)
    crew = Column(String(255), nullable=False)
    cast = Column(String(255), nullable=False)
    story = Column(LONGTEXT, nullable=False)
    host = Column(String(255), nullable=False)
    plan = Column(String(255), nullable=False)
    seats = Column(Integer, nullable=False)
    created_at = Column(DATETIME, nullable=False, server_default=func.now())
    updated_at = Column(DATETIME, nullable=False, server_default=func.now())

    performance_datetime = relationship('PerformanceDatetime', back_populates='performance')
    performance_person = relationship('PerformancePerson', back_populates='performance')
    performance_price = relationship('PerformancePrice', back_populates='performance')


class PerformanceDatetime(Base):
    __tablename__ = 'performance_datetime'
    __table_args__ = (
        ForeignKeyConstraint(['performance_id'], ['performance_item.id'], name='performance_datetime_performance_id_1b981785_fk_performan'),
        Index('performance_datetime_performance_id_1b981785_fk_performan', 'performance_id')
    )

    id = Column(BigInteger, primary_key=True)
    day = Column(String(20), nullable=False)
    time = Column(String(20), nullable=False)
    created_at = Column(DATETIME, nullable=False, server_default=func.now())
    updated_at = Column(DATETIME, nullable=False, server_default=func.now())
    performance_id = Column(BigInteger, nullable=False)

    performance = relationship('PerformanceItem', back_populates='performance_datetime')



class PerformancePerson(Base):
    __tablename__ = 'performance_person'
    __table_args__ = (
        ForeignKeyConstraint(['performance_id'], ['performance_item.id'], name='performance_person_performance_id_a778bb34_fk_performan'),
        Index('performance_person_performance_id_a778bb34_fk_performan', 'performance_id')
    )

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)
    chosung = Column(String(2), nullable=False)
    type = Column(String(20), nullable=False)
    created_at = Column(DATETIME, nullable=False, server_default=func.now())
    updated_at = Column(DATETIME, nullable=False, server_default=func.now())
    performance_id = Column(BigInteger, nullable=False)

    performance = relationship('PerformanceItem', back_populates='performance_person')


class PerformancePrice(Base):
    __tablename__ = 'performance_price'
    __table_args__ = (
        ForeignKeyConstraint(['performance_id'], ['performance_item.id'], name='performance_price_performance_id_d6e3b485_fk_performance_item_id'),
        Index('performance_price_performance_id_d6e3b485_fk_performance_item_id', 'performance_id')
    )

    id = Column(BigInteger, primary_key=True)
    price = Column(Integer, nullable=False)
    created_at = Column(DATETIME, nullable=False, server_default=func.now())
    updated_at = Column(DATETIME, nullable=False, server_default=func.now())
    performance_id = Column(BigInteger, nullable=False)

    performance = relationship('PerformanceItem', back_populates='performance_price')


class PerformanceFaculty(Base):
    __tablename__ = "performance_faculty"

    id = Column(BigInteger, primary_key=True)
    faculty_id = Column(String(20), nullable=False)
    faculty_name = Column(String(255), nullable=False)
    area = Column(String(20), nullable=False)
    seatscale = Column(Integer, nullable=False)
    address = Column(String(255), nullable=False)
    created_at = Column(DATETIME, nullable=False, server_default=func.now())
    updated_at = Column(DATETIME, nullable=False, server_default=func.now())
