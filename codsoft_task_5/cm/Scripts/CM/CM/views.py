import mysql.connector as sql
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def dashboard(request):
    con = sql.connect(host="localhost", database="CM",
                      user="root", password="root")
    
    params={'name':[],'phone':[], 'email':[]}
    if not con.is_connected():
        print("not connected")
        p = {"value": "serverdb"}
        return render(request, "redirect.html", p)
    else:
        try:
            mycur = con.cursor()
            mycur.execute(f"select * from sorted_contacts")
            data=mycur.fetchall()
            for i in range(len(data)):
                params['name'].append(data[i][0]+" " + data[i][1])
                params['phone'].append(data[i][3])
                params['email'].append(data[i][2])
            # print(params)
            con.commit()
            con.close()
            user_data = [{'name': name, 'phone':phone,'email': email} for name, phone, email in zip(params['name'], params['phone'], params['email'])]
            result = {'user_data': user_data}
            return render(request, "dashboard.html", result)
        except Exception as e:
            print(e)
            p = {"alertValue": "server"}
            return render(request, "dashboard.html", p)

def add(request):
    return render(request, 'add.html')

def delete(request):
    return render(request, 'delete.html')

def edit(request):
    return render(request, 'edit.html')

def update(request):
    return render(request, 'update.html')

def search(request):
    return render(request, 'search.html')

def forgotpassword(request):
    return render(request, 'forgotpassword.html')

def Redirect(request):
    return render(request, 'index.html')


def Login(request):
    con = sql.connect(host="localhost", database="CM",
                      user="root", password="root")
    if not con.is_connected():
        print("not connected")
        p = {"value": "serverdb"}
        return render(request, "login.html", p)
    else:
        if request.method == "POST":
            usr = request.POST.get('usr', 'n')
            pwd = request.POST.get('pwd', 'n')
            if usr!='n' and pwd!='n':
                request.session['user_name'] = usr
                mycur = con.cursor()
                mycur.execute(f"select * from users where username='{usr}' and password='{pwd}'")
                data = mycur.fetchone()
                con.commit()
                con.close()
                if data!= None:
                    request.session['user_name'] = usr
                    p = {"alertValue": "login"}
                    return render(request, "login.html", p)
                else:
                    p = {"alertValue": "loginuns"}
                    return render(request, "login.html", p)
            else:
                p = {"alertValue": "server"}
                return render(request, "login.html", p)
        p = {"alertValue": "django"}
        return render(request, 'login.html',p)

def SignUp(request):
    con = sql.connect(host="localhost", database="CM",
                      user="root", password="root")
    if not con.is_connected():
        print("not connected")
        p = {"value": "serverdb"}
        return render(request, "signup.html", p)
    else:
        if request.method == "POST":
            nm = request.POST.get('nm', 'n')
            eml = request.POST.get('eml', 'n')
            usr = request.POST.get('usr', 'n')
            pwd = request.POST.get('pwd', 'n')
            cpwd = request.POST.get('cpwd', 'n')

            if pwd == cpwd:
                if nm!='n' and eml!='n' and usr!='n' and pwd!='n':
                    mycur = con.cursor()
                    mycur.execute(f"insert into users values('{nm}','{eml}','{usr}','{pwd}')")
                    con.commit()
                    con.close()
                    p = {"alertValue": "signup"}
                    return render(request, "signup.html", p)
                else:
                    p = {"alertValue": "server"}
                    return render(request, "signup.html", p)
            else:
                p = {"alertValue": "pwdnomatch"}
                return render(request, "signup.html", p)
        p = {"value": "django"}
        return render(request, 'signup.html',p)

def Add(request):
    con = sql.connect(host="localhost", database="CM",
                      user="root", password="root")
    if not con.is_connected():
        print("not connected")
        p = {"value": "serverdb"}
        return render(request, "add.html", p)
    else:
        if request.method == "POST":
            fn = request.POST.get('fn', 'n')
            ln = request.POST.get('ln', 'n')
            pn = request.POST.get('pn', 'n')
            em = request.POST.get('em', 'n')
            img = request.POST.get('img', 'n')

            if fn!='n' and ln!='n' and pn!='n' and em!='n' and img!='n':
                mycur = con.cursor()
                try:
                    mycur.execute(f"insert into contacts values('{fn}','{ln}','{em}','{pn}','{img}')")
                    procedure_name = "UpdateSortedContacts"
                    mycur.callproc(procedure_name)
                    con.commit()
                    con.close()
                    p = {"alertValue": "add"}
                    return render(request, "add.html", p)
                except Exception as e:
                    print("\n\n",e,"\n\n    ")
                    p = {"alertValue": "repeat"}
                    return render(request, "add.html", p)    
            else:
                p = {"alertValue": "adduns"}
                return render(request, "add.html", p)
        p = {"value": "django"}
        return render(request, 'add.html',p)


def Delete(request):
    con = sql.connect(host="localhost", database="CM",
                      user="root", password="root")
    if not con.is_connected():
        print("not connected")
        p = {"value": "serverdb"}
        return render(request, "delete.html", p)
    else:
        if request.method == "POST":
            dd = request.POST.get('del', 'n')

            if dd!='n':
                mycur = con.cursor()
                try:
                    mycur.execute(f"delete from contacts where first_name='{dd}' or phone='{dd}'")
                    temp = mycur.rowcount
                    if temp > 0:
                        p = {"alertValue":"deleted"}
                        mycur.execute(f"delete from sorted_contacts where first_name='{dd}' or phone='{dd}'")
                        con.commit()
                        con.close()
                        return render(request, "delete.html", p)
                    elif temp == 0:
                        p = {"alertValue":"nocontact"}
                        return render(request, "delete.html", p)
                except Exception as e:
                    print(e)
                    p = {"alertValue": "server"}

                    return render(request, "delete.html", p)
                
            else:
                p = {"alertValue": "nodatatodel"}
                return render(request, "delete.html", p)
        p = {"value": "django"}
        return render(request, 'delete.html',p)


def Search(request):
    con = sql.connect(host="localhost", database="CM",
                      user="root", password="root")
    if not con.is_connected():
        print("not connected")
        p = {"value": "serverdb"}
        return render(request, "search.html", p)
    else:
        if request.method == "POST":
            sd = request.POST.get('searchData', 'n')

            if sd!='n':
                mycur = con.cursor()
                try:
                    mycur.execute(f"select * from contacts where first_name='{sd}' or phone='{sd}'")
                    data=mycur.fetchone()
                    con.commit()
                    con.close()
                    if data!=None:
                        result={'name': data[0]+" "+data[1], 'phone':data[3], 'email':data[2]}
                        return render(request, "show.html", result)
                    else:
                        p = {"alertValue": "nocontact"}
                        return render(request, "search.html", p)
                except Exception as e:
                    print(e)
                    p = {"alertValue": "server"}
                    return render(request, "search.html", p)
                
            else:
                p = {"alertValue": "nodatasearch"}
                return render(request, "search.html", p)
        p = {"value": "django"}
        return render(request, 'search.html',p)

def Edit(request):
    if request.method == "POST":
        # Check if the request contains search data
        search_data = request.POST.get('searchData', 'n')
        if search_data != 'n':
            # Connect to the database
            con = sql.connect(host="localhost", database="CM", user="root", password="root")
            if not con.is_connected():
                p = {"value": "serverdb"}
                return render(request, "redirect.html", p)
            else:
                try:
                    # Execute the search query
                    mycur = con.cursor()
                    mycur.execute(f"SELECT * FROM contacts WHERE first_name='{search_data}' OR phone='{search_data}'")
                    data = mycur.fetchone()
                    con.commit()
                    con.close()
                    if data is not None:
                        # If contact is found, pass the data to the template
                        result = {'name': data[0], 'last_name': data[1], 'phone': data[3], 'email': data[2]}
                        return render(request, "edit.html", {'result': result})
                    else:
                        # If contact is not found, return an appropriate message
                        p = {"alertValue": "nocontact"}
                        return render(request, "edit.html", p)
                except Exception as e:
                    print(e)
                    # If an error occurs during the database operation, return an error message
                    p = {"alertValue": "server"}
                    return render(request, "edit.html", p)
        else:
            # If no search data is provided, return a message indicating no data for search
            p = {"alertValue": "nodatasearch"}
            return render(request, "edit.html", p)
    else:
        # If it's a GET request, simply render the edit.html template
        return render(request, 'edit.html')
    #return render(request, 'redirect.html')

def ForgotPassword(request):
    return render(request, 'redirect.html')

def Update(request):
    con = sql.connect(host="localhost", database="CM",
                      user="root", password="root")
    if not con.is_connected():
        print("not connected")
        p = {"value": "serverdb"}
        return render(request, "redirect.html", p)
    else:
        if request.method == "POST":
            newname = request.POST.get('newname', 'n')
            newusername = request.POST.get('newusername', 'n')
            newemail = request.POST.get('newemail', 'n')
            oldpassword = request.POST.get('oldpassword', 'n')
            newpassword = request.POST.get('newpassword', 'n')
            cnewpassword = request.POST.get('confirmnewpassword', 'n')
            currentuser=request.session.get('user_name', 'n')
            if newname!='n' and newusername!='n' and newemail!='n' and oldpassword!='n' and newpassword!='n' and cnewpassword!='n':
                mycur = con.cursor()
                try:
                    mycur.execute(f"select * from users where username='{currentuser}' and password='{oldpassword}'")
                    data=mycur.fetchone()
                    if data != None:
                        if newpassword == cnewpassword:
                            mycur.execute(f"update users set name='{newname}', email='{newemail}', username='{newusername}', password='{newpassword}' where username='{currentuser}'")
                            if mycur.rowcount>0:
                                con.commit()
                                con.close()
                                request.session['user_name'] = newusername
                                p = {"alertValue": "updatesuc"}####
                                return render(request, "update.html", p)
                            else:
                                con.commit()
                                con.close()
                                p = {"alertValue": "updateuns"}###
                                return render(request, "update.html", p)
                        else:
                            p = {"alertValue": "pwdnomatch"}###
                            return render(request, "update.html", p)
                    else:
                        p = {"alertValue": "oldpwdwrong"}####
                        return render(request, "add.html", p)
                except Exception as e:
                    print("\n\n",e,"\n\n    ")
                    p = {"alertValue": "server"}
                    return render(request, "update.html", p)    
            else:
                p = {"alertValue": "nodatatoupdate"}
                return render(request, "add.html", p)
        p = {"value": "django"}
        return render(request, 'update.html',p)
    