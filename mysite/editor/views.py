from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request = request,
                template_name = 'editor/home.html')

def editor(request):
    if request.method == "POST":
        # a = 1
        # print the uploded file
        uploadedFile = request.FILES['document']
        fs = FileSystemStorage()
        image_name = fs.save(uploadedFile.name,uploadedFile)
        image_url = fs.url(image_name)
        data = {}
        data['image_url'] = image_url
        print(data)
        return render(request,'editor/editor.html',data)
    else:
        # Ask to upload the file
        return render(request,'editor/editor.html')