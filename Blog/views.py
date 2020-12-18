from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from  .models import *
from datetime import date

# Create your views here.
def all_cat():
    all_cat = Category.objects.all()
    return all_cat

def All_need_value():
    all_post = Post.objects.all().order_by('-id')
    recent = all_post[:3]
    li = []
    pos = []
    for i in all_post:
        a = i.post_like_set.count()
        li.append(a)
    for i in all_post:
        if max(li)>0:
            a = max(li)
            ind = li.index(a)
            li.pop(ind)
            li.insert(ind,0)
    top_three = pos[:3]
    return recent,top_three


def Home(request):

    log = False
    if request.user.is_authenticated():
        log = True

    all_post = Post.objects.all()
    li = []
    b = 0
    for i in all_post:
        a = Post_like.objects.filter(post = i)
        for j in a:
            b +=j.like
        li.append(b)
        b = 0
    z = zip(all_post,li)
    recent,top_three = All_need_value()
    d = {'all_cat':all_cat(),'all_post':z,'logout':log,'recent':recent,'top_three':top_three }
    return render(request,'index.html',d)

def about(request):
    log = False
    if request.user.is_authenticated():
        log = True
    d = {'all_cat':all_cat(),'logout':log}
    return render(request,'about.html',d)

def lifestyle(request):
    log = False
    if request.user.is_authenticated():
        log = True
    d = {'all_cat': all_cat(),'logout':log}
    return render(request,'lifestyle.html',d)
def fashion(request):
    log = False
    if request.user.is_authenticated():
        log = True
    d = {'all_cat': all_cat(),'logout':log}
    return render(request,'fashion.html',d)


def contact(request):
    log = False
    if request.user.is_authenticated():
        log = True
    d = {'all_cat': all_cat(),'logout':log}
    return render(request,'contact.html',d)

def Login(request):
    log = False
    if request.user.is_authenticated():
        log = True

    error = False
    if request.method == 'POST':
        u= request.POST['user']
        p =request.POST['pswd']
        user = authenticate(username= u, password = p)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error = True
    d = {'erorr':error,'logout':log}
    return render(request,'login.html',d)

def Singup(request):
    log = False
    if request.user.is_authenticated():
        log = True
    erorr = False


    if request.method == 'POST':
        n = request.POST['name']
        u = request.POST['username']
        e = request.POST['email']
        p = request.POST['pswd']
        user = User.objects.filter(username= u)
        if user:
            erorr= True
        else:
            User.objects.create_user(username=u, email=e, password=p, first_name=n)
            return redirect('Login')
    d = {'erorr':erorr,'all_cat':all_cat(),'logout':log}


    return render(request,'signup.html',d)


def Logout(request):
    log = False
    if request.user.is_authenticated():
        log = True
    d = {'logout':log}

    logout(request)
    return redirect('Login')

def blog_life(request,pid):
    if not request.user.is_authenticated():
        return redirect('Login')

    post = Post.objects.get(id = pid)
    data = Post_like.objects.filter(post = post).first()
    data2 = Post_like.objects.filter(post = post, user = request.user).first()

    if data2:
        return redirect('home')
    else:

        if data and data2:

            data.like +=1
            data.save()

        else:
            Post_like.objects.create(post = post, like = 1, user = request.user)

    return redirect('home')

def add_post(request):


    if request.method == 'POST' and request.user.is_authenticated():
        catygory = request.POST['cid']
        u = request.user
        T = request.POST['title']
        S = request.POST['subtitle']
        i = request.FILES['image']
        dis = request.POST['discrep']
        dat = date.today()
        cat = Category.objects.get(id=catygory)
        Post.objects.create(category=cat,User=u,title=T,subtitle= S,image= i,date= dat,discription= dis)
        return redirect('userdetail')

    d = {'all_cat': all_cat()}
    return render(request,'addpost.html',d)

def blogdetail(request,bid):

    blog_deatail = Post.objects.get(id = bid)
    d = {'all_cat': all_cat(),'detail':blog_deatail}

    return render(request,'singlepage.html',d)

def blog_comment(request,bid):
    if not request.user.is_authenticated():
        return redirect('Login')
    post = Post.objects.get(id = bid)
    if request.method == 'POST':

        c = request.POST['Message']
        Comment.objects.create(post=post, user=request.user, comment=c)
        return redirect('blogdetail',bid)

def userdetails(request):

    data = Post.objects.filter(User =request.user )

    d = {'data':data}
    return render(request,'fashion.html',d)

def delete_blog(request,bid):
    data = Post.objects.get(id =bid )
    data.delete()
    return redirect('userdetail')

def catygiory_post(request,cid):
    data =Category.objects.get(id=cid)
    all_post = data.post_set.all
    d = {'all_cat': all_cat(),'data':all_post,'cat':data}

    return render(request,'category_post.html',d)









