import io
import pandas as pd
import requests

service_key = "558a2759bba4416eab2d0f4d1f22a773"


def get_performance_list() -> list[dict]:
    """
    newsql -> "Y" 로 설정해야 "area" 결과 반환
    :return:
    """
    url = "http://kopis.or.kr/openApi/restful/pblprfr"
    params = {
        "service": service_key,
        "stdate": "20240209",
        "eddate": "20240210",
        "newsql": "Y",
        "cpage": 1,
        "rows": 10
    }
    response = requests.get(url, params=params)
    results = pd.read_xml(io.StringIO(response.text))

    return [results.loc[i].to_dict() for i in results.index]


def get_performance_detail(mt20id: str) -> dict:
    """
    :param mt20id:
    :return:
    """
    url = f"http://www.kopis.or.kr/openApi/restful/pblprfr/{mt20id}"
    params = {
        "service": service_key,
        "newsql": "Y"
    }
    response = requests.get(url, params=params)
    results = pd.read_xml(io.StringIO(response.text))

    return results.loc[0].to_dict()


def get_faculty_detail(mt10id: str) -> dict:
    url = f"http://kopis.or.kr/openApi/restful/prfplc/{mt10id}"
    params = {
        "service": service_key,
        "newsql": "Y"
    }
    response = requests.get(url, params=params)
    results = pd.read_xml(io.StringIO(response.text))

    return results.loc[0].to_dict()


if __name__ == "__main__":
    pf_detail = get_performance_detail("PF132236")
    print(pf_detail)
