from django.shortcuts import redirect, render,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
import requests 
from django.contrib import messages
# Create your views here.
def landing_page(request):
    posts=Post.objects.all()
    return render(request,"index.html",{
        "posts":posts
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
            
            
            post.save()
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
            return redirect('landing-page')  # Redirect after a successful upload
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
    return render(request,'post_page.html',{
        'post':post
    })  