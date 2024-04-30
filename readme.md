# Bot Discord - Documentation

Ce bot Discord a été développé pour fournir plusieurs fonctionnalités utiles à un serveur Discord. Il utilise la bibliothèque discord.py pour interagir avec l'API Discord.

## Fonctionnalités

### Salutations de bienvenue
Lorsqu'un nouveau membre rejoint le serveur, le bot envoie un message de bienvenue dans le salon de bienvenue par défaut.

### Commandes interactives
Le bot répond à plusieurs commandes interactives :

- !ping: Répond avec "pong 🏓" pour tester la latence du bot.
- !touché: Répond avec "coulé ! 💥" pour une interaction amusante.
- !members: Affiche une liste des membres du serveur avec leurs rôles.

### Blagues aléatoires
Le bot peut également envoyer des blagues aléatoires en utilisant l'API de blagues.

- !joke: Envoie une blague aléatoire suivie de sa réponse dans un format spoiler.

### Modération automatique
Le bot peut détecter un mot spécifique dans les messages et bannir automatiquement l'utilisateur qui l'a envoyé.

## Configuration

### Jetons d'API
Assurez-vous de fournir les jetons d'API nécessaires pour que le bot fonctionne correctement :
- tokenBlague: Jeton d'API pour accéder à l'API de blagues.
- bot.run(): Jeton d'authentification du bot Discord.

### Intents
Les intents ont été activés pour permettre au bot de recevoir des événements comme les messages et les connexions de membres.

- Tous les intents sont activés (intents = discord.Intents().all()).

## Utilisation

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances en exécutant `pip install -r requirements.txt`.
3. Remplacez les jetons d'API dans le code par vos propres jetons.
4. Exécutez le script Python pour lancer le bot.

## Auteurs

Ce bot Discord a été développé par [Heniart Loan](https://github.com/Lheniart).

