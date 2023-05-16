from flask import Blueprint, render_template

routes_bp = Blueprint("routes", __name__)

@routes_bp.route("/")
def index():
    return render_template("index.html", page_title='Início')

@routes_bp.route("/pedido")
def pedido():
    return render_template("pedido.html", page_title='Pedido')

@routes_bp.route("/comidas")
def comidas():
    return render_template("comidas.html", page_title='Comidas')

@routes_bp.route("/bebidas")
def bebidas():
    return render_template("bebidas.html", page_title='Bebidas')

@routes_bp.route("/sobremesas")
def sobremesas():
    return render_template("sobremesas.html", page_title='sobremesas')

@routes_bp.route("/login")
def login():
    return render_template("login.html", page_title='login')