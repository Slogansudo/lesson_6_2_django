from django.shortcuts import render
from django.http import HttpResponse


def choose_language(request):
    return HttpResponse("""<h1>choose language<h1>
    <div>
     <a href='http://127.0.0.1:8000/uzb/' target='_blank'>UZB</a>
     </div>
     <a href='http://127.0.0.1:8000/english/' target='_blank'>ENG</a>""")


def library_view(request):
    return render(request, 'libr_data2.html')
