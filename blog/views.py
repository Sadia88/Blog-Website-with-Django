from django.shortcuts import render, HttpResponse,redirect,HttpResponseRedirect
from .models import Post, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse

def blogHome(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)



def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "blog/blogPost.html", context)

def blogComment(request):
    return redirect(request,"blog/blogPost.html")




def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        comment=BlogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")

# The code that we've written above will only help us to post a comment and not to display the already posted comments. 

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post)
    context={'post':post, 'comments': comments, 'user': request.user}
    return render(request, "blog/blogPost.html", context)


def delete(request, id):
    comment = BlogComment.objects.filter(sno=id)
    comment.delete()
    # return redirect("blog/blogPost.html")
    # return HttpResponseRedirect("blog/blogPost.html")
    return HttpResponseRedirect(reverse('blogHome'))
    # return render(request, "blog/blogPost.html")
    