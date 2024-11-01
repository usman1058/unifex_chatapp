from django.shortcuts import redirect, render,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
import requests 
from django.contrib import messages
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
    return render(request,'post_page.html',{
        'post':post,
         "commentform":commentform,
         "replyform":replyform
    }) 
@login_required
def comment_sent(request,pk):
    post = get_object_or_404(Post, id=pk)
    
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid:
            comment=form.save(commit=False)
            comment.auther=request.user
            comment.parent_post=post
            comment.save()
            
    return redirect('post-page', post.id)

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
    
    if request.method == 'POST':
        form=ReplyForm(request.POST)
        if form.is_valid:
            reply=form.save(commit=False)
            reply.auther=request.user
            reply.parent_comment=comment
            reply.save()
            
    return redirect('post-page', comment.parent_post.id)

def reply_delete(request,pk):
    reply=get_object_or_404(Reply,id=pk,auther=request.user)
    if request.method == 'POST':
        reply.delete()
        messages.success(request,'Reply Deleted')
        return redirect('post-page',reply.parent_comment.parent_post.id)
    return render(request,"reply_delete.html",{
        "reply":reply 
    })
