from kopis_util import get_performance_list, get_performance_detail, get_faculty_detail, get_faculty_list
from batch.database.query import insert_performance, insert_faculty


def main():
    # performances = get_performance_list()
    # for performance in performances:
    #     performance_detail = get_performance_detail(performance["mt20id"])
    #     faculty_detail = get_faculty_detail(performance_detail["mt10id"])
    #     insert_performance(performance_detail, faculty_detail)

    faculty_list = get_faculty_list()
    for faculty in faculty_list:
        faculty_detail = get_faculty_detail(faculty["mt10id"])
        insert_faculty(faculty, faculty_detail)


if __name__ == "__main__":
    main()
    print("batch finish")