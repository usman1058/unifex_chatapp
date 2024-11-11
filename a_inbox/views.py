from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *
from a_users.models import *
from django.db.models import Q
from django.http import HttpResponse,Http404

# Create your views here.
@login_required
def inbox_view(request,conversation_id=None):
    my_conversation=Conversation.objects.filter(participants=request.user).order_by('-lastmessage_created')
    if conversation_id:
        conversation=get_object_or_404(my_conversation,id=conversation_id)
    else:
        conversation=None
    context={
        'conversation':conversation,
        'my_conversation':my_conversation
    }
    return render(request, 'a_inbox/inbox.html',context)

def search_user(request):
    letters=request.GET.get('search_user')
    if request.htmx:
        if len(letters) > 0:
            profile=Profile.objects.filter(displayname__icontains=letters).exclude(displayname=request.user.profile.displayname)
            users_id=profile.values_list('user',flat=True)
            users=User.objects.filter(
                Q(username__icontains=letters) | Q(id__in=users_id)).exclude(username=request.user.username)
            return render(request,'a_inbox/list_searchuser.html',{
                'users':users
            })
        else:
             return HttpResponse('')
    else:
        raise Http404()
    
@login_required
def new_message(request,recipient_id):
    recipient=get_object_or_404(User,id=recipient_id)
    new_message_form=InboxMessagesForm()
    
    if request.method=='POST':
        form=InboxMessagesForm(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.sender=request.user
            
            my_conversations=request.user.conversations.all()
            for c in my_conversations:
                if recipient in c.participants.all():
                    message.conversation =c
                    message.save()
                    c.lastmessage_created=timezone.now()
                    c.save()
                    return redirect('inbox',c.id)
            new_conversation=Conversation.objects.create()
            new_conversation.participants.add(request.user,recipient)
            new_conversation.save()
            message.conversation=new_conversation
            message.save()
            return redirect('inbox',new_conversation.id)
        
    context={
        'recipient':recipient,
        'new_message_form':new_message_form
    }
    return render(request,'a_inbox/form_newmessage.html',context)

@login_required
def new_reply(request,conversation_id):
    new_message_form=InboxMessagesForm()
    my_conversations=request.user.conversations.all()
    conversation=get_object_or_404(my_conversations,id=conversation_id)
    
    
    if request.method=='POST':
        form=InboxMessagesForm(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.sender=request.user
            message.conversation=conversation
            message.save()
            conversation.lastmessage_created=timezone.now()
            conversation.save()
            return redirect('inbox',conversation.id)
    
    context={
        'new_message_form':new_message_form,
        'conversation':conversation
    }
    return render(request,'a_inbox/form_newreply.html',context)

    
    