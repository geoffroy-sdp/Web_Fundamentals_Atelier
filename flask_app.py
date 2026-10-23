# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask, render_template, request, abort

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return render_template("accueil.html")


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------

@app.get("/presentation")
def presentation():
    return render_template("presentation.html", prenom="Valentin", nom="Kiri", loisirs=["Jeux vidéo", "Musique", "Escalade"])

@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return f"<h1>Bonjour {prenom} !</h1>"

@app.get("/calcul")
def calcul():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
    except ValueError:
        abort(400, description="Les paramètres a et b doivent être des nombres entiers.")

    operation = request.args.get("op", "plus")
    operations = {
        "plus": ("+", lambda: a + b),
        "moins": ("-", lambda: a - b),
        "fois": ("×", lambda: a * b),
        "divise": ("÷", lambda: a / b if b else abort(
            400, description="La division par zéro n'est pas autorisée."
        )),
    }
    if operation not in operations:
        abort(400, description="L'opération doit être plus, moins, fois ou divise.")

    symbole, calculer = operations[operation]
    return f"{a} {symbole} {b} = {calculer()}"

@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")


@app.get("/salut")
def salut():
    prenom = request.args.get("prenom", "inconnu")
    ville = request.args.get("ville", "nulle part")
    return f"Bonjour {prenom}, qui vient de {ville} !"

# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
