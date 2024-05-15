from flask import Flask, render_template, request, session
from datafile import filename

import os

from classes.hotel import Hotel
from classes.quarto import Quarto
from classes.reservaquarto import ReservaQuarto
from classes.faturareserva import FaturaReserva
from classes.fatura import Fatura
from classes.userlogin import Userlogin

app = Flask(__name__)

Userlogin.read(filename + 'hotel.db')
Hotel.read(filename + 'hotel.db')
Quarto.read(filename + 'hotel.db')
Fatura.read(filename + 'hotel.db')
ReservaQuarto.read(filename + 'hotel.db')
FaturaReserva.read(filename + 'hotel.db')



prev_option = ""
submenu = ""
app.secret_key = 'BAD_SECRET_KEY'

# upload_folder = os.path.join('static', 'ProductFotos')
# app.config['UPLOAD'] = upload_folder


import subs_login as lsub
import subs_gform as gfsub
import subs_gformT as gfTsub
import subs_hform as gfhsub
import subs_subform as gfsubsub
#import subs_productFoto as productFotosub
import subs_signup as signupsub
import subs_hoteis as hoteissub

@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
    
@app.route("/login")
def login():
    return lsub.login()

@app.route("/logoff")
def logoff():
    return lsub.logoff()

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    return lsub.chklogin()

@app.route("/register/<cname>", methods=["post","get"])
def register(cname=''):
    submenu = request.args.get("subm")
    return signupsub.registerform(cname,submenu)

@app.route("/submenu", methods=["post","get"])
def getsubm():
    global submenu
    submenu = request.args.get("subm")
    return render_template("index.html", ulogin=session.get("user"),submenu=submenu)

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname=''):
    submenu = request.args.get("subm")
    return gfsub.gform(cname,submenu)

@app.route("/gformT/<cname>", methods=["post","get"])
def gformT(cname=''):
    submenu = request.args.get("subm")
    return gfTsub.gformT(cname,submenu)

@app.route("/hform/<cname>", methods=["post","get"])
def hform(cname=''):
    submenu = request.args.get("subm")
    return gfhsub.hform(cname,submenu)


        
@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname=""):
    submenu = request.args.get("subm")
    return gfsubsub.subform(cname,submenu)


# @app.route("/productform", methods=["post","get"])
# def productFoto():
#     submenu = request.args.get("subm")
#     cname = 'Product'
#     return productFotosub.productFoto(app,cname,submenu)

@app.route("/order/mapa", methods=["post","get"])
def ordermapa():

    return render_template("uc.html", ulogin=session.get("user"),submenu=submenu)

@app.route("/hoteis", methods=["post","get"])
def hoteisform(cname='Hotel'):
    submenu = request.args.get("subm")
    return hoteissub.hoteisform(cname,submenu)

  
if __name__ == '__main__':
    app.run(debug=True)
    #app.run()