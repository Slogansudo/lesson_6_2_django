
from django.http import HttpResponse


def homepage(request):
    return HttpResponse("""<h2>Hello developers, welcome to my first web application<h2>
    <a href="http://127.0.0.1:8000/library/" target="_blank"> library_page</a>
    <div> 
        <a href="http://127.0.0.1:8000/users/" target="_blank"> user_page</a>
    </div""")
