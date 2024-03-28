from django.shortcuts import render


def library_view2(request):
    return render(request, 'libr_data1.html')
