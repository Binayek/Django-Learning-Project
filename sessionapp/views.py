from django.shortcuts import render, redirect

"""def set_session(request):
    request.session["username"]='John'
    request.session['age']=25
    return redirect('get_session')

def get_session(request):
    username=request.session.get('username','Guest')
    age=request.session.get('age','Not set')
    return render(request,"show.html",{'username':username,'age':age})

def delete_session(request):
    request.session.flush()
    return redirect('get_session')"""


def set_cookie(request):
    response =HttpResponse("Cookie Set")
    request.set_cookie('username','John',max_age=3600)
    return response

def get_cookie(request):
    username =request.COOKIES.get('username',"Guest")
    return Httpresponse(f"Username:{username}")

def delete_cookie(request):
    response= HttpResponse("Cookie Deleted")
    response.delete_cookie('username')
    return response
# Create your views here.
