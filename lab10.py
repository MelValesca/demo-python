from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def form () :
    return render_template("lab10.html")

@app.route("/submit", methods=["POST"])
def submit () :
    nom = request.form["nom"]
    prenom = request.form["prenom"]
    age = request.form["age"]

    erreur = ""

    if not nom :
        erreur += "- Le nom ne doit pas être vide.\n"
    if not prenom :
        erreur += "- Le prénom ne doit pas être vide.\n"
    if not age :
        erreur += "- L'âge ne doit pas être vide.\n"

    if erreur == "" :
        log = open("log.txt", "a", encoding="utf8")
        log.write(nom + ", " + prenom + ", " + age + "\n")
        log.close()
        return redirect("/resultats")
    else :
        return render_template("lab10.html", erreur=erreur, nom=nom, prenom=prenom, age=age)
    
@app.route("/resultats")
def resultats () :
    resultats = []
    log = open("log.txt", "r", encoding="utf8")
    lignes = log.readlines()
    log.close()

    for ligne in lignes :
        decouper = ligne.split(", ") # split apres chaque virgule ["nom", "prenom", "age"]
        resultats.append(decouper)
    
    return render_template("tableau.html", resultats=resultats, len=len(resultats))