from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

# Create your views here.
@login_required
def image_created(request):
    if request.method=='POST':
        # form is sent
        form = ImageCreateForm(data= request.POST)
        if form.is_valid():
            # form data is valid
            cd= form.cleaned_data
            new_image= form.save(commit=False)
            # Assign the current user to the item
            new_image.user= request.user
            new_image.save()
            messages.success(request, 'Image added successfu;ly')
            # Redirect to new created item detail view
            return redirect(new_image.get_absolute_url())
    else:
        # build form with data provided by the bookmarks via GET
        form= ImageCreateForm(data= request.GET)
    return render(request, 'images/image/create.html',
                    {'section': 'images',
                    'form': form})