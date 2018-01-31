from django.shortcuts import render, redirect
from time import gmtime, strftime
import re
import random
import bcrypt
from django.contrib import messages
from models import *

def index(request):

    return render(request, "poke/index.html")

def pokes(request):
    print "----QUOTE HOME"
    print "session ", request.session.values()

    usr = User.objects.get(id=request.session['uid'])

    all_pokes = usr.poked.all().order_by('-count')
    poke_count = usr.poked.all().count()

    all_users = User.objects.all()

    # print "pokes: ", all_pokes
    # print "users: ", all_users

    context = {
        'all_pokes': all_pokes,
        "poke_count": poke_count,
        'all_users': all_users,
    }
    # print context
    return render(request, "poke/pokes.html", context)

def add_poke(request, uid):
    print ('--- add poke ---')
    print request.session.values()

    p_from = User.objects.get(id = request.session['uid'])
    p_to = User.objects.get(id=uid)

    print " from: ", p_from.id
    print " to: ", p_to.id

    # exist, get poke object, add to count
    p = p_from.pokes.filter(poke_to = p_to)
    print p, len(p)

    if not p: 
        # create new poke
        print " create new poke =="
        p = Poke.objects.create(poke_from=p_from, poke_to=p_to)
        print "count: ", p.count
        tot_cnt = p_to.tot_count
        tot_cnt += 1
        p_to.tot_count = tot_cnt
        p_to.save()
        return redirect('/pokes')
    else:
        print "count before:", p[0].count
        cnt = p[0].count
        cnt += 1
        p[0].count = cnt
        p[0].save()

        tot_cnt = p_to.tot_count
        tot_cnt += 1
        p_to.tot_count = tot_cnt
        p_to.save()

        print p[0].count
        return redirect('/pokes')  

# def show_user(request, uid):
#     usr = User.objects.get(id = request.session['uid'])

#     qt = usr.quotes.all()
#     cnt = usr.quotes.count()
#     nm = usr.name

#     context = {
#         'all_quotes': qt,
#         'count': cnt,
#         'name': nm,
#     }

#     return render(request, "poke/show_user.html", context)

def register(request):
    if request.method == 'POST':
        print " Post "
        #validate data

        print request.POST
        print "---validate data ---"
        errors = User.objects.validate(request.POST)

        print errors
        if (errors):
            print "==== errror "
            for error in errors:
                messages.error(request, errors[error])
            print messages
            return render(request, "poke/index.html")
        print "===== no errors ==="
        
        print "====  create user ===="
        # hash password
        hashPWD = bcrypt.hashpw(request.POST['pwd'].encode(), bcrypt.gensalt())

        # check to see if email has been used
        usr = ''
        try:
            usr = User.objects.get(email=request.POST['email'])
        except Exception as e:
            print e, str(type(e))
            # no user in db, register user
    
            # create new user
            newUser = User.objects.create(name = request.POST['name'], alias = request.POST['alias'], email = request.POST['email'], pwd = hashPWD, dob=request.POST['dob'])
            print " newUser: ", newUser
            request.session['user'] = newUser.name
            request.session['uid'] = newUser.id

        if usr:
            messages.error(request, "Error: Email has previously used to register another user.  Please use another email.")
            return render(request, "poke/index.html")
        
        return redirect('/pokes')
    return render(request, "poke/index.html")

def login(request):
    if request.method == 'POST':
        print "---sign in validate data ---"

        errors = User.objects.validate(request.POST)
        print "-- error: ", errors
        if (errors):
            print "==== errror "
            for error in errors:
                messages.error(request, errors[error])
            print messages
            return redirect("/login")
        print "===== no errors ==="
        
        usr = ''

        try:
            usr = User.objects.get(email = request.POST['email'])
        except Exception as e:
            print e, str(type(e))
            messages.error(request, "Error: Invalid User")
            return render(request, "poke/index.html")

        if usr:
            valid = bcrypt.checkpw(request.POST['pwd'].encode(), usr.pwd.encode())
            if (valid):
                print "password match"
                request.session['uid'] = usr.id
                request.session['user'] = usr.name
            else:
                messages.error(request, "Error: Invalid Password")
                return redirect('/login')
                # return render(request, "quotes/login.html")    
        print request.session.values()
        return redirect('/pokes')
    return render(request, "poke/index.html")

def success(request):
    return render(request, 'poke/success.html')

def reset(request):
    request.session.clear()
    return redirect('/main')