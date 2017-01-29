from django.shortcuts import render
from .forms import BookForm

def  home(request):
    form = BookForm
    if request.method == 'POST':
        print (form)
    return render(request, 'form.html',{'form': form})
    
    
