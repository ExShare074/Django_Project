from django.shortcuts import render

def data_view(request):
    return render(request, 'data_app/data.html')

def test_view(request):
    return render(request, 'data_app/test.html')
