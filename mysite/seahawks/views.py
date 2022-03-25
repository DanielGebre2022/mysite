
from django.shortcuts import render, get_object_or_404;
from .models import Author, Book, Publisher;
from django.urls import reverse_lazy;
from .forms import AuthorForm, PublisherForm;
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'seahawks/index.html')

def publisher(request):
    publisher_list=Publisher.objects.all()
    return render(request, 'seahawks/publisher.html', {'publisher': publisher_list})

def author(request):
    author_list=Author.objects.all()
    return render(request, 'seahawks/author.html', {'author_list': author_list})

def book(request, id):
    book=get_object_or_404(Book, pk=id)
    return render(request, 'seahawks/book.html', {'book': book})
@login_required
def newPublisher(request):
    form=PublisherForm

    if request.method=='POST':
        form=PublisherForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=PublisherForm()
    else:
        form=PublisherForm()
    return render(request, 'mysite/newpublisher.html', {'form': form})

def newAuthor(request):
    form=AuthorForm

    if request.method=='POST':
        form=AuthorForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=AuthorForm()
    else:
        form=AuthorForm()
    return render(request, 'mysite/newauthor.html', {'form': form})

def loginmessage(request):
    return render(request, 'seahawks/loginmessage.html')

def logoutmessage(request):
    return render(request, 'seahawks/logoutmessage.html')
# Create your views here.
