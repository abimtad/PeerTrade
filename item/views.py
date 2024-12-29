from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewItemForm, EditItemForm
from .models import Item, Category
from django.db.models import Q

def new(request):
	if request.method == 'POST':
		form = NewItemForm(request.POST, request.FILES)

		if form.is_valid():
			item = form.save(commit=False)
			item.owner = request.user

			item.save()

			return redirect('item:detail', pk=item.id)
	else:
		form = NewItemForm()
	
	return render(request, 'item/new.html', {
		'form': form
	})


def detail(request, pk):
	item = get_object_or_404(Item, pk=pk)
	related_items = Item.objects.filter(category=item.category)

	return render(request, 'item/detail.html', {
		'item':item,
		'related_items': related_items,
		'title': item.name,
	})


def edit(request, pk):
	item = get_object_or_404(Item, pk=pk)
	if request.method == 'POST':
		form = EditItemForm(request.POST, request.FILES, instance=item)

		if form.is_valid():
			form.save()

			return redirect('item:detail', pk=pk)
	else:
		form = EditItemForm(instance=item)

	return render(request, 'item/edit.html', {
		'form': form,
	})

def delete(request, pk):
	item = Item.objects.get(id=pk)
	item.delete()

	return redirect('core:dashboard')


def browse(request):
	query = request.GET.get('query', '')
	items = Item.objects.filter(is_sold=False)
	categories = Category.objects.all()
	category_id = request.GET.get('category', 0)
	
	if category_id:
		if query:
			items = Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query), category=category_id)
		else:
			items = Item.objects.filter(category=category_id)
	else:		
		print(query)
		if query:
			items = Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

	return render(request, 'item/browse.html', {
		'query': query,
		'items': items,
		'categories': categories,
		'category_id': category_id,
	})