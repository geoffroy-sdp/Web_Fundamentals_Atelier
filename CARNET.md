# 📒 Mon carnet de bord

**Nom :** SDP

**Prénom :** Geoffroy

**Adresse de mon site :** https://merzouz.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse : PythonAnywhere

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse :_ Parce que le site tourne sur le cloud de pythonanywhere

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse :_ Le nom d'hôte est`www.google.com` et le chemin est `/maps`.

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse :_ « Not Found » veut dire que le serveur ne trouve pas la page demandée.

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse :_ Flask utilise le nom de la fonction comme nom de route interne donc si il y en a 2, sa casse et flash donne une err au demarrage

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse :_ Le serveur envoie du texte contenant du HTML. Le navigateur interprète les balises et affiche une page mise en forme au lieu d'afficher le code tel quel.

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse :_ `<h1>` représente un titre principal, `<p>` un paragraphe, `<ul>` une liste non ordonnée et `<li>` un élément de cette liste.

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse :_ L'image est hébergée sur un autre serveur. Le navigateur lit son adresse dans l'attribut `src` et la télécharge depuis ce serveur.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse :_ Cela sépare la logique du site et sa présentation

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse :_ C'est le serveur qui remplace `{{ prenom }}` avec le moteur de templates

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse :_ Le HTML décrit la structure, le CSS définit son apparence

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse :_ deux fichiers : le document HTML et la feuille CSS

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse :_ Le navigateur peut garder l'ancienne feuille de style dans son cache. Ctrl + F5 force le rechargement des fichiers

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ HTTP signifie « HyperText Transfer Protocol ». Le navigateur envoie la requête et le serveur renvoie la réponse.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ deux fichiers : le document HTML et la feuille CSS

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ `200` signifie que la requête a réussi. `404` car il ne trouve pas la favicon

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ Ces modifications ne changent que l'affichage dans mon navigateur, elles sont en local

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ Le nom du paramètre est `search_query` et sa valeur est `chat`.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ Le serveur essaie de convertir `bonjour` en entier avec `int()`, Il faut vérifier les données recues et gérer les valeurs invalides.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ La valeur pourrait contenir du HTML ou du JS malveillant, pour eviter les injection xss.

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ Avec GET, les données apparaissent dans l'URL après le `?`. Avec POST, elles sont envoyées dans le corps de la requête

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ GET convient à une recherche, car l'URL peut être partagée. Pour une connexion, POST évite de mettre le mot de passe dans l'URL

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ Non. Les données POST restent visibles dans les outils de développement

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ Une erreur 4xx indique un problème client. Une erreur 5xx indique un problème serveur

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ Le serveur renvoie une réponse 3xx avec une adresse `Location`. Le navigateur lit cette adresse puis envoie lui-même une deuxième requête.

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ Un site peut rediriger une ancienne adresse vers une nouvelle, ou rediriger une adresse HTTP vers HTTPS.

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ Le serveur peut recevoir mon adresse IP, le type de navigateur et de système indiqué par le User-Agent

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?
salut
   > _Ma réponse :_ Wikipédia peut utiliser cet en-tête pour proposer une version du site dans une langue que le navigateur préfère

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ À compléter avec le chemin exact lu dans mon Access log, par exemple `/favicon.ico` si c'est cette requête qui apparaît avec le code 404.

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ La navigation n'est pas totalement anonyme : le serveur reçoit des informations techniques et peut enregistrer les visites.

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ Une page HTML contient des balises que le navigateur interprète pour afficher du contenu à une personne. Une réponse JSON contient des données structurées, surtout destinées à être échangées et lues par des programmes.

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ Le serveur exécute les routes Flask et produit la page `/horloge` ainsi que les données JSON de `/api/heure`. Le navigateur exécute le JavaScript : il appelle l'API, lit le JSON et met à jour l'heure dans la page.

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ Une application météo utilise une API : elle envoie une ville ou une position et reçoit des données

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ Quand on saisit une adresse, le navigateur trouve le serveur correspondant et lui envoie une requête HTTP(S). Le serveur traite la demande et renvoie une réponse, par exemple du HTML. Le navigateur interprète ce HTML, télécharge au besoin les fichiers liés comme le CSS ou les images, puis affiche la page.
