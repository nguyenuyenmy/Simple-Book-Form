from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BookForm, AuthorForm
from .models import Book, Author
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json


def index(request):
    form_book = BookForm(request.POST or None)
    if form_book.is_valid():
        form_book.save()
        return HttpResponseRedirect('/')
    return render(request, 'form_app/index.html', {'form_book': form_book})


def author(request):
    form_author = AuthorForm(request.POST or None)
    if form_author.is_valid():
        instance = form_author.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_author");</script>' % (instance.pk, instance))
    return render(request, 'form_app/author_page.html', {'form_author': form_author})


def AuthorEditPopup(request, pk=None):
    instance = get_object_or_404(Author, pk=pk)
    form_author = AuthorForm(request.POST or None, instance=instance)
    if form_author.is_valid():
        instance = form_author.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_author");</script>' % (instance.pk, instance))
    return render(request, 'form_app/author_page_edit.html', {'form_author': form_author})


def AuthorDeletePopup(request, pk=None):
    instance = get_object_or_404(Author, pk=pk)
    form_author = AuthorForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        instance.delete()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_author");</script>' % (instance.pk, instance))
    return render(request, 'form_app/author_page_delete.html', {'form_author': form_author})


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@csrf_exempt
def get_author_id(request):
    if is_ajax(request=request):
        author_name = request.GET['author_name']
        author_id = Author.objects.get(author_name=author_name).id
        data = {'author_id': author_id}
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse("/")
