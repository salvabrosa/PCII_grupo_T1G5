# -*- coding: utf-8 -*-

import datetime

from flask import Flask, render_template, request, session
from classes.hotel import Hotel
from classes.quarto import Quarto
from classes.reservaquarto import ReservaQuarto
from classes.faturareserva import FaturaReserva
from classes.fatura import Fatura
from classes.userlogin import Userlogin
from classes.tiposquarto import TiposQuarto

prev_option = ""

def reservaquartoform(cname='',submenu=""):
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        cl = eval(cname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        user_notfound = 0
        falta_atributo = 0
        erro_datas = 0
        erro_formato_datas = 0
        if prev_option == 'insert' and option == 'save':
            if (cl.auto_number == 1):
                strobj = "None"
            else:
                strobj = request.form[cl.att[0]]
            for i in range(1,len(cl.att)-2):
                if request.form[cl.att[i]] == "" :
                    falta_atributo = 1
                if cl.att[i] == '_codigo_cliente':
                    if request.form[cl.att[i]] not in Userlogin.lst:
                        user_notfound = 1
                    else: 
                        strobj += ";" + request.form[cl.att[i]]
                elif cl.att[i] == '_codigo_quarto':
                    if request.form[cl.att[i]] not in Userlogin.lst:
                        user_notfound = 1
                    else: 
                        strobj += ";" + request.form['_codigo_cliente']
                elif cl.att[i] == '_checkin':
                    try:
                        datetime.date.fromisoformat(request.form[cl.att[i]])
                        strobj += ";" + request.form[cl.att[i]]
                    except ValueError:
                        erro_formato_datas = 1    
                elif cl.att[i] == '_checkout':
                    try:
                        datetime.date.fromisoformat(request.form[cl.att[i]])
                        strobj += ";" + request.form[cl.att[i]]
                    except ValueError:
                        erro_formato_datas = 1      
                else:
                    strobj += ";" + request.form[cl.att[i]]
            if request.form['_checkin'] >= request.form['_checkout'] and falta_atributo == 0:   
                erro_datas = 1
            if user_notfound == 0 and falta_atributo == 0 and erro_datas == 0 and erro_formato_datas == 0:
                obj = cl.from_string(strobj)
            cl.last()
        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            # if auto_number = 1 the key stays the same
            for i in range(1,len(cl.att)):
                att = cl.att[i]
                setattr(obj, att, request.form[att])
            cl.update(getattr(obj, cl.att[0]))
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
            obj['_pequenoalmoco'] = 'False'
            obj['_estado_reserva'] = 'False'
        return render_template("reservaquarto.html", butshow=butshow, butedit=butedit, 
                        cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                        ulogin=session.get("user"),auto_number=cl.auto_number,
                        submenu=submenu,tipou=session.get("tipouser"),
                        prev_option = prev_option, option = option,
                        user_notfound = user_notfound, falta_atributo = falta_atributo, erro_datas = erro_datas,
                        erro_formato_datas = erro_formato_datas)
    else:
        return render_template("index.html", ulogin=ulogin)