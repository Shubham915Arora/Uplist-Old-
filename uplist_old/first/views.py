from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import loc,ad,cat,message
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    catdata = cat.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email_id']
        password = request.POST['password']
        
        x = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                     password=password)
        #profile=userprofile(profilepic=pic)
        data = userprofile(User=x)
        #profile.save
        data.save()
        print("user created")
        return redirect('index page')

    else:
        return render(request, 'form.html',{'cat':catdata})


def login(request):
    catdata = cat.objects.all()
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']

        from django.contrib import auth
        x = auth.authenticate(username=username1, password=password1)
        if x is None:
            return redirect('Login')

        else:
            auth_login(request, x)
            return redirect('index page')



    else:
        return render(request, 'login.html',{'cat':catdata})

@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    return redirect('./')

def index(request):
    catdata = cat.objects.all()
    addata = ad.objects.all()


    if request.method=='POST':
        search=request.POST['Search']
        if ad.objects.get(ad_name=search):
            print(search)
            addata=ad.objects.get(ad_name=search)
            return render(request, 'single-product.html/addata.id/', {'ad': addata})
    else:

        return render(request, 'index.html',{'cat': catdata,'ad':addata})


def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='/login/')
def adpost(request):
    if request.method == 'POST':
        ad_title = request.POST['ad_title']
        ad_posted_by = request.user.id
        ad_price = request.POST['ad_price']
        ad_loc = request.POST['ad_loc']
        ad_image1 =request.FILES.get('ad_image1')
        ad_image2 =request.FILES.get('ad_image2')
        ad_image3 =request.FILES.get('ad_image3')
        ad_image4 =request.FILES.get('ad_image4')
        ad_des = request.POST['ad_desc']
        ad_cat= request.POST['ddlcat']

        ad_data= ad(ad_name=ad_title, ad_posted_by=User.objects.get(pk=ad_posted_by), ad_price=ad_price, ad_loc=loc.objects.get(pk=ad_loc),
              img1=ad_image1, img2=ad_image2, img3=ad_image3, img4=ad_image4,
              ad_des=ad_des, ad_cat=cat.objects.get(pk=ad_cat))

        ad_data.save();
        return redirect('index page')
    else:
        catdata=cat.objects.all()
        locdata=loc.objects.all()
        return render(request, 'postad.html',{'cat': catdata,'loc': locdata})

def products(request):
    addata=ad.objects.all()
    return render(request,'products.html',{'ad': addata})

@login_required(login_url='/login/')
def changepassword(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        newpass1 = request.POST['new_Password']

        from django.contrib import auth
        if auth.authenticate(username=username1, password=password1) :
            data=User.objects.get(username=username1)
            data.password(request.POST.get('newpass1'))
            data.save()

        if x is None:
            return redirect('changepass')

        else:
            return redirect('./')

    else :
        return render(request, 'changepass.html')

def categories(request):
    catdata = cat.objects.all()
    return render(request, 'categories.html',{'cat': catdata})

def singlead(request,ad_id=None):
    addata = ad.objects.get(pk=ad_id)
    catid = addata.ad_cat
    rads = ad.objects.filter(ad_cat=catid)
    #ad_cat=ad.objects.filter(ad_cat=ad_id)
    return render(request,'single-product.html',{'ad':addata,'cat':rads})

@login_required(login_url='/login/')
def sendmessage(request,ad_id=None):
    catdata=cat.objects.all()
    if request.method== 'POST':
        addata = ad.objects.get(pk=ad_id)
        msg_subj = request.POST['Subject']
        msg_from = request.user.id
        msg_to = addata.ad_posted_by
        print("to",msg_to)
        print("from",msg_from)
        msg_content = request.POST['Message']
        msg_data = message(msg_regarding=msg_subj,msg_content=msg_content,msg_from=User.objects.get(pk=msg_from),msg_to=User.objects.get(username=msg_to),msg_ad=ad.objects.get(pk=addata.id))
        msg_data.save()
        return redirect('/')
    else:
        addata = ad.objects.get(pk= ad_id)
        return render(request, 'single-product.html', {'ad': addata,'cat':catdata})

def productscat(request, id=None):
    catdata=cat.objects.all()
    addata = ad.objects.filter(ad_cat=id)
    return render(request,'products.html',{'ad':addata,'cat':catdata})

def about(request):
    return render(request, 'about.html')

@login_required(login_url='/login/')
def chatbox(request, id=None):
    catdata = cat.objects.all()
    msgdata = message.objects.filter(msg_ad=id)
    return render(request,'chatbox.html',{'msg':msgdata})

def search(request):
    catdata = cat.objects.all()
    query = request.GET['search']
    all_ads = ad.objects.get(ad_name=query)
    catid=all_ads.ad_cat
    rads= ad.objects.filter(ad_cat=catid)
    # params = {'all_ads': all_ads}
    return render(request, 'search_ad.html', {'ad':all_ads,'cat':rads})
    # return HttpResponse('this is search')

@login_required(login_url='/login/')
def mypostedad(request):
    catdata = cat.objects.all()
    msgby = request.user
    addata = ad.objects.filter(ad_posted_by=msgby)
    return render(request,'mypostedad.html', {'ad':addata, 'user':msgby,'cat':catdata})

@login_required(login_url='/login/')
def deletedata(request,id=None):
    ad.objects.filter(id=id).delete()
    return redirect('ADs Posted')

@login_required(login_url='/login/')
def changedata(request,id=None):

    addata=ad.objects.get(pk=id)
    if request.method=='POST':
        ad_title = request.POST['ad_title']
        ad_price = request.POST['ad_price']
        ad_loc = request.POST['ad_loc']
        ad_des = request.POST['ad_desc']
        ad_cat = request.POST['ddlcat']
        ad_image1 =request.FILES.get('ad_image1')
        ad_image2 =request.FILES.get('ad_image2')
        ad_image3 =request.FILES.get('ad_image3')
        ad_image4 =request.FILES.get('ad_image4')

        addata.ad_name = ad_title
        addata.ad_price = ad_price
        addata.ad_loc = loc.objects.get(pk=ad_loc)
        addata.ad_des = ad_des
        addata.ad_cat = cat.objects.get(pk=ad_cat)
        addata.img1=ad_image1
        addata.img2 = ad_image2
        addata.img3 = ad_image3
        addata.img4 = ad_image4


        addata.save()
        return redirect('ADs Posted')



    else:
        catdata = cat.objects.all()
        locdata = loc.objects.all()
        return render(request,'changedata.html',{'cat': catdata,'loc': locdata,'ad':addata})

def userprofile(request):
    return render(request, 'userprofile.html')