from django.shortcuts import render, redirect
from .models import Movies
from .forms import MovieCreate
from django.http import HttpResponse


# DataFlair
def index(request):
    shelf = Movies.objects.all()
    return render("<h1>dfsdf</h1>")


def upload(request):
    upload = MovieCreate()
    if request.method == 'POST':
        upload = MovieCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'book/upload_form.html', {'upload_form': upload})


def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Movies.objects.get(id=book_id)
    except Movies.DoesNotExist:
        return redirect('index')
    book_form = MovieCreate(request.POST or None, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    return render(request, 'book/upload_form.html', {'upload_form': book_form})


def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Movies.objects.get(id=book_id)
    except Movies.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')
