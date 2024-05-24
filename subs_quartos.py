# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: subs_gform.py

"""""
from werkzeug.utils import secure_filename
import os

from flask import Flask, render_template, request, session
from classes.hotel import Hotel
from classes.quarto import Quarto
from classes.reservaquarto import ReservaQuarto
from classes.faturareserva import FaturaReserva
from classes.fatura import Fatura
from classes.userlogin import Userlogin
from classes.tiposquarto import TiposQuarto
from classes.reserva2Form import Reserva2Form

prev_option = ""
img = ""

def quartosform(cname='',submenu=""):
    global prev_option
    global img
    ulogin=session.get("user")
    hotel_notfound = 0
    erro_andar = 0
    if (ulogin != None):
        cl = eval(cname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if prev_option == 'insert' and option == 'save':
            if (cl.auto_number == 1):
                strobj = "None"
            else:
                strobj = request.form[cl.att[0]]
            for i in range(1,len(cl.att)-1):
                # ERRO NA CRIAÇÃO DO QUARTO 
                if cl.att[i] == '_cod_hotel':
                    if request.form[cl.att[i]] not in Hotel.lst:
                        hotel_notfound = 1
                        break
                    else:
                        strobj += ";" + request.form[cl.att[i]]
                if cl.att[i] == '_andar':
                    if request.form[cl.att[i]] == "" or int(request.form[cl.att[i]]) not in Hotel.obj[request.form['_cod_hotel']].lista_andares:
                        erro_andar = 1
                        break
                    else:
                        strobj += ";" + request.form[cl.att[i]]
                else:
                    strobj += ";" + request.form[cl.att[i]]
            else: 
                
                obj = cl.from_string(strobj)
                cl.insert(getattr(obj, cl.att[0]))
                cl.last()
        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            # if auto_number = 1 the key stays the same
            for i in range(cl.auto_number,len(cl.att)-1):
                att = cl.att[i]
                if att != '_andar':
                    setattr(obj, att, request.form[att])
            # DINAMICO PRECO DE QUARTO
            setattr(obj, '_preco_noite', TiposQuarto.obj[obj._tipoquarto]._preco_noite)
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
                return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = cl.current()
        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            for att in cl.att:
                obj[att] = ""
            obj['_cod_hotel'] = 'H1'
            obj['_tipoquarto'] = '1'
            obj['_preco_noite'] = ''            
            
        return render_template("quartos.html", butshow=butshow, butedit=butedit,
                        cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                        ulogin=session.get("user"),auto_number=cl.auto_number,
                        submenu=submenu,tipou=session.get("tipouser"),
                        prev_option = prev_option, option = option,
                        Hotel = Hotel.obj, TiposQuarto = TiposQuarto.obj,
                        hotel_notfound = hotel_notfound, erro_andar = erro_andar)
    else:
        return render_template("index.html", ulogin=ulogin)
