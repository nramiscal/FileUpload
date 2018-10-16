from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

def handle_uploaded_file(file, filename):
    with open('apps/myApp/media/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)



def index(request):
    return render(request, 'myApp/index.html')

def upload_file(request):
    if request.FILES:
        print('file received')
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
    else:
        print('no file :(')
    return redirect('/')
