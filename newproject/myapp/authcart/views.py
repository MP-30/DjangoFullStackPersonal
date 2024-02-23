from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def signup(request):
  # print("i am running the signup function")
  if (request.method=="POST"):
    email=request.POST['email']
    password=request.POST['pass1']
    confirm_password=request.POST['pass2']
    if password != confirm_password:
      messages.warning(request, "Password is not matching")
      # return HttpResponse("password incorrect")
      return render(request,'signup.html')
    
    try:
      if User.objects.get(username=email):
       # return HttpResponse("email already exist")
        messages.info(request,"Email is Taken")
        return render(request,'signup.html')
      
    except Exception as identifier:
      pass
 
    user = User.objects.create_user(email,email,password)
    user.is_active=False
    user.save()
    email_subject="Activate Your Account"
    message=render_to_string('activate.html',{
        'user':user,
        'domain':'10.138.149.94:5000',
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':generate_token.make_token(user)

    })
    
    return HttpResponse("User created", email)
  return render(request,"signup.html")

def handlelogin(request):
  return render(request, "login.html")

def handlelogout(request):
  return redirect('/auth/login')