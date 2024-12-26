from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewItemForm
from .models import Item, Category

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