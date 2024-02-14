import re
from datetime import datetime
from jamo import h2j, j2hcj


def remove_dot(item: str) -> str:
    return item.replace(".", "")


def parse_age(x):
    x = re.sub(r'만| |이상', '', x)
    age = 0
    if '전체' in x:
        age = 0
    elif '개월' in x:
        age = int(x.split('개월')[0])//12
    elif '세' in x:
        age = int(x.split('세')[0])
    return age


def parse_story(text: str) -> str:
    text_list = re.split(r'\n|\r', text)
    text_list = [t for t in text_list if t != '']
    return "\n".join(text_list)


def parse_price(price: str) -> int:
    digit_string = ''.join([ch for ch in price if ch.isdigit()])
    return int(digit_string) if digit_string else 0


DAYS = {0: "월요일", 1: "화요일", 2: "수요일", 3: "목요일", 4: "금요일", 5: "토요일", 6: "일요일"}
DAYS_inverse = {v: k for k, v in DAYS.items()}


def parse_datetimes(time_str) -> list[str, str]:
    # example)  화요일 ~ 금요일(20:00), 토요일(15:00,17:30,20:00), 일요일(15:30,18:00)

    results = []
    time_list = time_str.split(", ")
    for t in time_list:
        open_point = t.find("(")
        day = t[:open_point]
        times = t[open_point:].replace("(", "").replace(")", "").split(",")
        if "~" in day:
            start_day, end_day = day.replace(" ", "").split("~")
            start_num, end_num = DAYS_inverse[start_day], DAYS_inverse[end_day]
            if end_num < start_num:
                end_num += 7
            for i in range(start_num, end_num + 1):
                day = DAYS[i%7]
                for time in times:
                    results.append([day, time])
        else:
            for time in times:
                results.append([day, time])

    return results

day_dict = {
    "Monday": " (월)",
    "Tuesday": " (화)",
    "Wednesday": " (수)",
    "Thursday": " (목)",
    "Friday": " (금)",
    "Saturday": " (토)",
    "Sunday": " (일)"
}
def parse_date_detail(date_from_str: str, date_to_str: str) -> str:
    date_from = datetime.strptime(date_from_str, "%Y.%m.%d")
    date_from_day = day_dict[datetime.strftime(date_from, "%A")]
    date_to = datetime.strptime(date_to_str,"%Y.%m.%d")
    date_to_day = day_dict[datetime.strftime(date_to, "%A")]
    return date_from_str + date_from_day + " ~ " + date_to_str + date_to_day


def parse_time(time: str):
    return time.replace("HOL", "공휴일")


def parse_chosung(ch: str) -> str:
    return j2hcj(h2j(ch))[0]


def parse_names(names: str) -> list[str]:
    results = []
    if names.endswith(" 등"):
        names = names[:-2]
    names = names.split(", ")
    for name in names:
        if name == "" or name == " ":
            continue
        else:
            results.append(name)
    return results


def parse_area(area: str) -> str:
    area = area[:2]
    if area == "부산" or area == "울산" or area == "대구":
        area = "경상"
    elif area == "대전":
        area = "충청"
    elif area == "광주":
        area = "전라"
    elif area == "인천":
        area = "경기"
    else:
        area = ""
    return area


def parse_enterprise(a, b):
    enterprise = set([a, b])
    enterprise = [e for e in enterprise if len(e) > 2]
    if len(enterprise) == 0:
        return ""
    else:
        return ', '.join(enterprise)


if __name__ == "__main__":
    parse_date_detail("2024.02.06", "2024.02.07")

    print(parse_chosung("삼"))