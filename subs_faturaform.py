# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: subs_gform.py

"""""
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

def faturaform(cname="",submenu=""):
    global prev_option
    tlist = cname.split('_')
    cnames = tlist[0]
    scname = tlist[1]   #+ "_" + tlist[2]         
    ulogin=session.get("user")
    user_notfound = 0
    falta_atributo = 0
    erro_formato_datas = 0
    falta_reserva = 0
    if (ulogin != None):
        cl = eval(cnames)
        sbl = eval(scname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        
        if prev_option == 'insert' and option == 'save':
            if (cl.auto_number == 1):
                strobj = "None"
            else:
                strobj = request.form[cl.att[0]]
            for i in range(1,len(cl.att)):
                if request.form[cl.att[i]] == "" :
                    falta_atributo = 1
                    break
                if cl.att[i] == '_cod_cliente':
                    if request.form[cl.att[i]] not in Userlogin.lst:
                        user_notfound = 1
                        break
                    else: 
                        strobj += ";" + request.form[cl.att[i]]
                elif cl.att[i] == '_dataemissao':
                    try:
                        datetime.date.fromisoformat(request.form[cl.att[i]])
                        strobj += ";" + request.form[cl.att[i]]
                    except ValueError:
                        erro_formato_datas = 1 
                else:
                    strobj += ";" + request.form[cl.att[i]]
            if user_notfound == 0 and falta_atributo == 0:
                obj = cl.from_string(strobj)
                cl.insert(getattr(obj, cl.att[0]))
                cl.last()
                
        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            # if auto_number = 1 the key stays the same
            for i in range(cl.auto_number,len(cl.att)):
                att = cl.att[i]
                setattr(obj, att, request.form[att])
            cl.update(getattr(obj, cl.att[0]))
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "delete":
                obj = cl.current()
                lines = sbl.getlines(getattr(obj, cl.att[0]))
                for line in lines:
                    sbl.remove(line)
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
            elif option[:6] == "delrow":
                row = int(option.split("_")[1])
                obj = cl.current()
                lines = sbl.getlines(getattr(obj, cl.att[0]))
                print(row,lines[row])
                sbl.remove(lines[row])
            elif option == "addrow":
                butshow = "disabled"
                butedit = "disabled"
                
            elif option == "saverow":
                obj = cl.current()
                strobj = getattr(obj, cl.att[0])
                for i in range(1,len(sbl.att)):
                    if sbl.att[i] == '_cod_reserva':
                        if request.form[sbl.att[i]] not in ReservaQuarto.lst:
                            falta_reserva = 1
                            break
                        else:
                            strobj += ";" + request.form[sbl.att[i]]
                    else:
                        strobj += ";" + request.form[sbl.att[i]]
                        
                if falta_reserva == 0:
                    objl = sbl.from_string(strobj)
                    code = str(getattr(objl, sbl.att[0])) + str(getattr(objl, sbl.att[1]))
                    sbl.insert(code)
                
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user")) 
        prev_option = option
        obj = cl.current()
        headers = list()
        objl = list()
        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            for att in cl.att:
                obj[att] = ""
        else:
            for i in range(1, len(sbl.att)): 
                    headers.append(sbl.att[i][1:])        
            lines = sbl.getlines(getattr(obj, cl.att[0])) 
            for line in lines:
                objl.append(sbl.obj[line])
        return render_template("faturaform.html", butshow=butshow, butedit=butedit,
                    cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                    ulogin=session.get("user"),objl=objl,headerl=sbl.header,
                    desl=sbl.des, attl=sbl.att, auto_number=cl.auto_number,
                    submenu=submenu,
                    user_notfound = user_notfound, falta_atributo = falta_atributo,
                    erro_formato_datas = erro_formato_datas, falta_reserva = falta_reserva)
    else:
        return render_template("index.html", ulogin=ulogin)