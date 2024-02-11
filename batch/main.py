from kopis_util import get_performance_list, get_performance_detail, get_faculty_detail
from batch.database.table.performance import insert_performance
from batch.database.table.performance_price import insert_prices
from batch.database.table.performance_datetime import insert_datetime
from batch.database.table.performance_person import insert_people


def main():
    performances = get_performance_list()
    for performance in performances:
        performance_detail = get_performance_detail(performance["mt20id"])
        faculty_detail = get_faculty_detail(performance_detail["mt10id"])
        insert_performance(performance_detail, faculty_detail)
        insert_prices(performance_detail)
        insert_datetime(performance_detail)
        insert_people(performance_detail)


if __name__ == "__main__":
    main()
    print("batch finish")