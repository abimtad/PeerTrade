from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ChatForm
from item.models import Item 
from .models import Conversation, ConvoMessage

@login_required
def newChat(request, pk):
	item = Item.objects.filter(pk=pk).first()

	conversation = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

	if conversation:
		return redirect('conversation:detail', pk=conversation.first().id)

	if request.method == 'POST':
		form = ChatForm(request.POST)
		
		if form.is_valid():
			new_conversation = 	Conversation.objects.create(item=item)

			new_conversation.members.add(item.owner)
			new_conversation.members.add(request.user)

			new_message = form.save(commit=False)

			new_message.conversation = new_conversation	
			new_message.created_by = request.user
			
			new_message.save()
			new_conversation.save()

			return redirect('conversation:detail', pk=new_conversation.id)


	else:
		form = ChatForm()
	
	return render(request, 'conversation/new.html', {
		'form': form,
		'recipient': item.owner,
	})


@login_required
def inbox(request):
	user = get_object_or_404(User, pk=request.user.id)
	conversations = user.conversations.all()

	return render(request, 'conversation/inbox.html', {
		'conversations': conversations,
	})

@login_required
def detail(request, pk):
	conversations = request.user.conversations.all()
	conversation = get_object_or_404(Conversation, pk=pk)
	recipient = conversation.members.exclude(id=request.user.id).first()
	messages = conversation.messages.all()

	if request.method == 'POST':
		form = ChatForm(request.POST)

		if form.is_valid():
				message = form.save(commit=False)
				message.conversation = conversation
				message.created_by = request.user

				message.save()	
				conversation.save()

				return redirect('conversation:detail', pk=conversation.id)
	else:
		form = ChatForm()		

	return render(request, 'conversation/detail.html', {
		'messages': messages,
		'conversation': conversation,
		'conversations': conversations,
		'recipient': recipient,
		'form': form,
		'pk': pk,
	})