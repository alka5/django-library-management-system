from django.shortcuts import render, get_object_or_404
from .form import Library_User, BookForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Book
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def create_librarian(request):
    forms = Library_User(request.POST or None, request.FILES or None)
    if forms.is_valid():
        if User.objects.filter(username=request.POST['username']).exists():
            msg = 'User Already Satisfied Or Try With Different Email'
            return render(request, 'signup.html', {'forms':forms,"msg" : msg})
        else:
            forms.save()
            return render(request, "signup.html", {'forms':forms,'msg':'User Created'})
    return render(request, "signup.html", {'forms':forms})

def librarian_login(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username =  request.POST["email"]
        password =  request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user.is_staff == False:
            logout(request)
            msg = 'You Do Not Have permission to Access'
            return render(request, 'login.html', {"msg" : msg})

        elif user is not None:
            login(request, user)
            return HttpResponseRedirect( reverse('book'))

def librarian_logout(request):
    logout(request)
    return HttpResponseRedirect( reverse('login'))


def home(request):
    all_book = Book.objects.all()
    return render (request, 'index.html',{'books':all_book})

def single_book(request,id):
    one_book = Book.objects.get(id=id)
    return render (request, 'single_book.html',{'book':one_book})

@staff_member_required(login_url='login')
def book_crud(request):
    all_book = Book.objects.all()
    if request.method == 'GET':
        form = BookForm()
        all_book = Book.objects.all()

        return render(request,'books_library.html',{'form':form,'books':all_book})
    
    if request.method == 'POST':
        form = BookForm(request.POST , request.FILES)
        if form.is_valid:
            form.save()
            msg = 'New Book added to Library'
            return render(request, 'books_library.html',{'form':form,'msg':msg,'books':all_book})


@staff_member_required(login_url='login')
def book_delet(request,id):
    book = Book.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('book'))

@staff_member_required(login_url='login')
def book_edit(request,id):
    if request.method =='GET':
        book_update = Book.objects.get(id=id)

        return render(request, 'update_delete.html',{'book':book_update})

@staff_member_required(login_url='login')
def book_u(request, id):
    instance=Book.objects.get(id=id)
    form = BookForm(request.POST or None , request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect (reverse('book'))
    return HttpResponse ('error')