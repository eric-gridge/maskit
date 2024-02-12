import math

from django.shortcuts import render

from .models import Performance


def performance_list(request):
    page_size = 2
    page = request.GET.get("page", 1)
    limit = page_size * int(page)
    offset = limit - page_size
    performances = Performance.objects.all()
    page_count = math.ceil(len(performances) / page_size)
    context = {
        "performances": performances[offset: limit],
        "page": page,
        "page_count": page_count,
        "page_range": range(1, page_count),  # [1,2,3,...,page_count-1]
    }
    return render(request, 'list.html', context)


def performance_detail(request, id):
    performance = Performance.objects.get(id=id)
    return render(request, 'detail.html', {'performance': performance})
