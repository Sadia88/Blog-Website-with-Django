from django.shortcuts import render,redirect, HttpResponse
from home.models import Contact,About
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
import json
from django.http import JsonResponse

# Create your views here.
def home(request):
 
   return render(request, 'home/home.html')

def ajax(request):

    return render(request,"home/ajax.html")

def about(request):
    allAbout= About.objects.all()
    # for e in About.objects.all():
    #     print(e)
    a=list(allAbout)
    print(allAbout)
    if request.method=="POST":
        authorId=request.POST['authorId']
        name=request.POST['name']
        email=request.POST['email']
        about =request.POST['about']
        if(authorId==''):
             author=About(name= name, email=email, about=about)
             
        else:
         author=About(id=authorId,name= name, email=email, about=about)

        author.save()
        # below 3 line is for corverting data into json formate
        a=About.objects.values()
        allAbout=list(a)
        # print(allAbout)
        print({'allAbout': allAbout})
        return JsonResponse({'allAbout': allAbout})
    allAbout={"allAbout": allAbout}
    return render(request,"home/about.html",allAbout)

def delete(request):
    if request.method=="POST":
        id=request.POST.get('sid')
        delPost= About.objects.get(pk=id)
        delPost.delete()
        return JsonResponse({"status":1})
    else:
        return JsonResponse({"status":0})
def edit(request):
    if request.method=="POST":
        id=request.POST.get('sid')
        editPost= About.objects.get(pk=id)
        editData={'id': editPost.id,'email':editPost.email,'name':editPost.name,'about':editPost.about}
        return JsonResponse(editData)
  
        


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)





def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('home')

        else:
         # Create the user
            # if len(username)<10:
            #    messages.error(request, " Your user name must be within 10 characters")
            #    return redirect('home')
               
            if not username.isalnum():
               messages.error(request, " User name should only contain letters and numbers")
               return redirect('home')
            if (pass1!= pass2):
               messages.error(request, " Passwords do not match")
               return redirect('home')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your My-Blog has been successfully created")
                 
        
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
