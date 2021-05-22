from django.shortcuts import render

# Create your views here.
def HomePage_views(request):

    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        print(name)
        print(email)
        print(text)
    return render(request,'home.html')