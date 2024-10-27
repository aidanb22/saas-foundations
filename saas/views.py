from django.http import HttpResponse
import pathlib
from django.shortcuts import render  # the proper convention'
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    """Home Page View returns a HTML  """
    my_title = "My Page"
    html_template = "home.html"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": page_qs.count() * 100.0 / qs.count(),
        "total_visit_count": qs.count(),
    }
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)


def my_old_home_page_view(request, *args, **kwargs):
    """Home Page View returns a HTML  """
    my_title = {
        "My Page"
    }
    my_context = {
        "page_title": my_title
    }

    html_ = """
            <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title></title>
        </head>
        <body>
            <h1> {page_title} anything?</h1>
        </body>
    </html>
    """.format(**my_context)
    return HttpResponse(html_)
