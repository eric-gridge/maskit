import math

from django.shortcuts import render

from .models import Item, Faculty


genre_dic = {"genre0": None, "genre1": "연극", "genre2": "뮤지컬", "genre3": "한국음악(국악)", "genre4": "서양음악(클래식)",
             "genre5": "대중음악", "genre6": "무용(서양/한국무용)", "genre7": "대중무용", "genre8": "서커스/마술", "genre9": "복합"}

area_dic = {"area0": None, "area1": "서울", "area2": "경기", "area3": "충청", "area4": "경상", "area5": "전라",
            "area6": "강원", "area7": "제주", "area8": "대학로"}

def performance_list(request):
    context = {}
    page_size = 15
    page = request.GET.get("page", 1)

    name = request.GET.get("name", None)
    genre = request.GET.get("genre", None)
    age = request.GET.get("age", None)
    price = request.GET.get("price", None)
    # price_from = request.GET.get("price_from", None)
    # price_to = request.GET.get("price_to", None)

    faculty_name = request.GET.get("faculty_name", None)
    area = request.GET.get("area", None)

    crew = request.GET.get("crew", None)
    cast = request.GET.get("cast", None)
    host = request.GET.get("host", None)
    plan = request.GET.get("plan", None)

    limit = page_size * int(page)
    offset = limit - page_size
    performances = Item.objects
    if name:
        context["name"] = name
        performances = performances.filter(name__icontains=name)
    if genre:
        context["genre"] = genre
        genre = genre_dic.get(genre, None)
        if genre:
            performances = performances.filter(genre=genre_dic.get(genre))
    if age:
        context["age"] = age
        performances = performances.filter(age__gte=int(age))
    if price:
        context["price"] = price
        performances = performances.filter(performance_price__price__gte=int(price))
    # if price_from:
    #     performances = performances.filter(performance_price__price__gte=price_from)
    # if price_to:
    #     performances = performances.filter(performance_price__price__lte=price_to)

    if faculty_name:
        context["faculty_name"] = faculty_name
        performances = performances.filter(faculty_name=faculty_name)
    if area:
        context["area"] = area
        area = area_dic.get(area, None)
        if area == "대학로":
            performances = performances.filter(daehakro="Y")
        elif area:
            performances = performances.filter(area=area)

    if crew:
        context["crew"] = crew
        print(crew)
        performances = performances.filter(performance_person__name=crew, performance_person__type="crew")
    if cast:
        context["cast"] = cast
        print(cast)
        performances = performances.filter(performance_person__name=cast, performance_person__type="cast")
    if host:
        context["host"] = host
        print(host)
        performances = performances.filter(host__icontains=host)
    if plan:
        context["plan"] = plan
        print(plan)
        performances = performances.filter(plan__icontains=plan)

    performances = performances.all()
    page_count = math.ceil(len(performances) / page_size)

    context["performances"] = performances[offset: limit]
    context["page"] = page
    context["page_count"] = page_count
    context["page_range"] = range(1, page_count)

    return render(request, 'list.html', context)


def performance_detail(request, id):
    performance = Item.objects.get(id=id)
    return render(request, 'detail.html', {'performance': performance})


def alarm(request):
    context = {}
    faculty_list = Faculty.objects
    name = request.GET.get("faculty_name", None)
    if name:
        faculty_list = faculty_list.filter(faculty_name__icontains=name)

    context["choosed_name"] = request.GET.get("choosed_name", "")

    context["faculty_list"] = faculty_list.all()
    return render(request, "alarm.html", context)