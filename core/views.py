from django.shortcuts import render, redirect
from item.models import Item, Category
from .forms import SignupForm

def index(request):

	items = Item.objects.filter(is_sold=False)
	categories = Category.objects.all()

	return render(request, 'core/index.html', {
		'items': items,
		'categories': categories,
		'title': 'New Items',
	})


def category(request, pk):
	category = Category.objects.filter(pk=pk).first()
	items = Item.objects.filter(is_sold=False, category=category)[:6]
	categories = Category.objects.all()

	return render(request, 'core/index.html', {
		'items': items,
		'categories': categories,
		'title': category.name,
	})


def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect('/login/')
	else:
		form = SignupForm()
	
	return render(request, 'core/signup.html', {
		'form': form,
	})


def dashboard(request):
	items = Item.objects.filter(owner=request.user)
	
	return render(request, 'core/dashboard.html', {
		'items': items,
	})


def contact(request):
	return render(request, 'core/contact.html', {
		'title': 'title',
	})

def about(request):
	return render(request, 'core/about.html', {
		'title': 'title',
	})


def privacy(request):
	return render(request, 'core/privacy.html', {
		'title': 'title',
	})
