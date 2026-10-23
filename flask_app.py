# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return "ahhh j'ai la flemmme"


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------

# exo 2
@app.get("/presentation")
def presentation():
    return """
    <h1>Léa Martin</h1>
    <p>Je m'appelle <strong>Valentin</strong> et j'aime le kiri et quand je pete sous l'eau sa fait des bulles</p>
    <h2>Ce que j'aime</h2>
    <ul>
        <li>Le kiri</li>
        <li>Les bubulles</li>
    </ul>
    <img src="https://imgs.search.brave.com/GKoxYvenmL0oEsdW4Bw0BjxROj9c2eEOaBKCNtsAaNA/rs:fit:0:180:1:0/g:ce/aHR0cHM6Ly9pLmlt/Z2ZsaXAuY29tLzQv/aWlrdHYuanBn" width="100">
    """


# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
