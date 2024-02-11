import re

BOOLEAN = {
    "Y": True,
    "N": False
}


def parse_boolean(item: str) -> bool:
    return BOOLEAN.get(item, False)  # default -> N


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


def parse_enterprise(enterprise_a, enterprise_b):
    if enterprise_a == enterprise_b:
        return enterprise_a
    else:
        if enterprise_a == "" or enterprise_a == " ":
            return enterprise_b
        elif enterprise_b == "" or enterprise_b == " ":
            return enterprise_a
        else:
            return enterprise_a + ", " + enterprise_b
