from django.shortcuts import redirect, render,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
import requests 
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.models import User
# Create your views here.
def landing_page(request,tag=None):
    if tag:
        posts=Post.objects.filter(tags__slug=tag)
        tag=get_object_or_404(Tag,slug=tag)
    else:
        posts=Post.objects.all()
        
    categories=Tag.objects.all()
    
    return render(request,"index.html",{
        "posts":posts,
        "categories":categories,
        'tag':tag
    })

    
@login_required
def post_create_wc(request):
    form=postCreateFrom()
    if request.method == "POST":
          form=postCreateFrom(request.POST)
          if form.is_valid:
            post= form.save(commit=False)
            # THIS IS A WEB CRAWLER
            website=requests.get(form.data['url'])
            sourcecode =BeautifulSoup(website.text,'html.parser')
            
            
            find_image=sourcecode.select('meta[content^="https://live.staticflickr.com/"]')
            image = find_image[0]['content']
            post.image = image
            
            
            find_title=sourcecode.select('h1.photo-title')
            title = find_title[0].text.strip()
            post.title =title
            
            
            find_artist=sourcecode.select('a.owner-name')
            artist = find_artist[0].text.strip()
            post.artist =artist
            
            post.auther=request.user
            
            post.save()
            form.save_m2m()
            return redirect('landing-page')
        
    return render(request,'post-create_ws.html',{
        'form':form
    })
    
def post_create(request):
    form=postCreationFrom()
    if request.method == "POST":
        form=postCreationFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('landing-page')
    return render(request,"post_create_simple.html",{
            'form':form,
        })
        
def post_delete(request,pk):
    post=get_object_or_404(Post,id=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request,'Post Deleted')
        return redirect('landing-page')
    return render(request,"post_delete.html",{
        "post":post
    })
    
    
def post_edit(request,pk):
    post=get_object_or_404(Post,id=pk)
    form = postEditForm(instance=post)
    if request.method == 'POST':
        form = postEditForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'Post updated')
            return redirect('landing-page')
    
    return  render(request,'post_edit.html',{
        'post':post,
        'form':form
    })      
    
def post_page(request,pk):
    post=get_object_or_404(Post,id=pk)
    commentform=CommentForm()
    replyform=ReplyForm()
    
    if request.htmx:
        if 'top' in request.GET:
            comments=post.comments.annotate(num_likes=Count('likes')).order_by('-num_likes')
        else:  
            comments=post.comments.all()
        return render(request,'snippets/loop_comments.html',{
            'comments':comments,
        })
    
    return render(request,'post_page.html',{
        'post':post,
         "commentform":commentform,
         "replyform":replyform
    }) 
@login_required
def comment_sent(request,pk):
    replyform=ReplyForm()
    post = get_object_or_404(Post, id=pk)
    
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid:
            comment=form.save(commit=False)
            comment.auther=request.user
            comment.parent_post=post
            comment.save()
            
    return render(request,"snippets/add_comment.html",{
        "comment":comment,
        "post":post,
        "replyform":replyform
    })

def comment_delete(request,pk):
    post=get_object_or_404(Comment,id=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request,'Comment Deleted')
        return redirect('post-page',post.parent_post.id)
    return render(request,"comment_delete.html",{
        "comment":post
    })
    
@login_required
def reply_sent(request,pk):
    comment = get_object_or_404(Comment, id=pk)
    replyform=ReplyForm()
    
    if request.method == 'POST':
        form=ReplyForm(request.POST)
        if form.is_valid:
            reply=form.save(commit=False)
            reply.auther=request.user
            reply.parent_comment=comment
            reply.save()
            
    return render(request,"snippets/add_reply.html",{
        "comment":comment,
        "reply":reply,
        "replyform":replyform
        
    })

def reply_delete(request,pk):
    reply=get_object_or_404(Reply,id=pk,auther=request.user)
    if request.method == 'POST':
        reply.delete()
        messages.success(request,'Reply Deleted')
        return redirect('post-page',reply.parent_comment.parent_post.id)
    return render(request,"reply_delete.html",{
        "reply":reply 
    })


def like_post(request,pk):
    post = get_object_or_404(Post, id=pk)
    user_exist=post.likes.filter(username=request.user.username).exists()
    
    if post.auther != request.user:
        if user_exist:
            post.likes.remove(request.user)
        else:   
            post.likes.add(request.user)
         
    return render(request,'snippets/likes.html',{
        'post':post,
    })
def like_comment(request,pk):
    comment = get_object_or_404(Comment, id=pk)
    user_exist=comment.likes.filter(username=request.user.username).exists()
    
    if comment.auther != request.user:
        if user_exist:
            comment.likes.remove(request.user)
        else:   
            comment.likes.add(request.user)
         
    return render(request,'snippets/likes_comment.html',{
        'comment':comment,
    })
def like_reply(request,pk):
    reply = get_object_or_404(Reply, id=pk)
    user_exist=reply.likes.filter(username=request.user.username).exists()
    
    if reply.auther != request.user:
        if user_exist:
            reply.likes.remove(request.user)
        else:   
            reply.likes.add(request.user)
         
    return render(request,'snippets/likes_reply.html',{
        'reply':reply,
    })