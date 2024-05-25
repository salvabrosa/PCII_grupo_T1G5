# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: subs_gform.py

"""""
from flask import Flask, render_template, request, session
from classes.hotel import Hotel
from classes.quarto import Quarto
from classes.reservaquarto import ReservaQuarto
from classes.faturareserva import FaturaReserva
from classes.fatura import Fatura
from classes.userlogin import Userlogin
from classes.tiposquarto import TiposQuarto

prev_option = ""

def usersform(cname='',submenu=""):
    global prev_option
    ulogin=session.get("tipouser")
    falta_atributo = 0
    user_existe = 0
    if (ulogin != None):
        cl = eval(cname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if prev_option == 'insert' and option == 'save':
            if request.form[cl.att[0]] in Userlogin.lst:
                user_existe = 1
                
            else:
                strobj = request.form[cl.att[0]]
            if user_existe == 0:
                for i in range(1,len(cl.att)):
                    if request.form[cl.att[i]] == '' :
                        falta_atributo = 1
                        
                    else:
    
                        if cl.att[i] == '_password':
                            strobj += ";" + Userlogin.set_password(request.form[cl.att[i]])
                        else:
                            strobj += ";" + request.form[cl.att[i]]
                if falta_atributo == 0 and user_existe == 0:
                    obj = cl.from_string(strobj)
                    cl.insert(getattr(obj, cl.att[0]))
                cl.last()
        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            # if auto_number = 1 the key stays the same
            for i in range(1,len(cl.att)-1):
                att = cl.att[i]
                if request.form[att] == "":
                    falta_atributo = 1
                if att == "_password" and falta_atributo == 0:
                    setattr(obj, "_password", Userlogin.set_password(request.form[cl.att[i]])) 
                elif falta_atributo == 0:                    
                    setattr(obj, att, request.form[att])
            if falta_atributo == 0:
                cl.update(getattr(obj, cl.att[0]))
            #EDITAR O TIPO DE UTILIZADOR APENAS SE FOR ADMIN
            if session.get("tipouser") == "admin":
                setattr(obj, '_usergroup', request.form['_usergroup'])
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "delete":
                obj = cl.current()
                cl.remove(getattr(obj, cl.att[0]))
                if not cl.previous():
                    cl.first()
            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"
            elif option == 'cancel':
                pass
            elif option == "first":
                cl.first()
            elif option == "previous":
                cl.previous()
            elif option == "next":
                cl.nextrec()
            elif option == "last":
                cl.last()
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"),tipou=session.get("tipouser"))
        prev_option = option
        obj = cl.current()
        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            for att in cl.att:
                obj[att] = ""
        return render_template("users.html", butshow=butshow, butedit=butedit,
                        cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                        ulogin=session.get("user"),auto_number=cl.auto_number,
                        submenu=submenu,tipou=session.get("tipouser"),
                        prev_option = prev_option, option = option,
                        falta_atributo = falta_atributo, user_existe = user_existe)
    else:
        return render_template("index.html", ulogin=ulogin)