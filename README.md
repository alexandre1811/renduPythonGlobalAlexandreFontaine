# Rendu Python Alexandre Fontaine

> ### **Route du Rendu Django** :
- Pour acceder au CRUD l'URL de l'index est : ``` / ```
- Pour acceder au Chat avec le WebSocket l'URL est : ``` /chat ```
- Pour acceder au mode Admin vue en cours l'URL est : ``` /admin ```

> ### **Ligne de commande pour le WebSockets de Django** :
- Installer Channels pour Python ``` python3 -c 'import channels; print(channels.__version__)' ```
- Installer Redis pour Channels avec pip``` pip3 install channels_redis ```
- Lancer le conteneur Docker de Redis ``` docker run -p 6379:6379 -d redis:5 ```

> ### **Ligne de commande pour lancer le serveur local Django** :
- Aller dans le dossier RenduDjango
- Executer la commande : ``` python3 manage.py runserver ```

> ### **Commande Du Jeu sur PyGame**
- Pour lancer le jeu en etant dans le dossier RenduPygame: ``` python3 main.py```
- Pour Tirer utilisez la touche ``` Espace ```
- Pour se Déplacer utilisez les touches ``` Z,Q,S,D``` ou les ``` Flèches Directionnelles ```

> ### **Objectif du jeu**
- **SURVIVRE**