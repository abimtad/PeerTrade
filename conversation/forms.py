from django import forms
from .models import ConvoMessage

class ChatForm(forms.ModelForm):
	class Meta:
		model = ConvoMessage
		fields = ('content',)
		widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 bg-gray-100 resize-none outline-none h-[59px]',
				'placeholder': 'Type a message...',
				'id': 'chatInput',
            })
        }	