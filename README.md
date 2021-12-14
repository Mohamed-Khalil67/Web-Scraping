# Web-Scraping

## Objectif du projet : Pour un client (fictif ou non) vous devez coder un script python qui permet d’extraire automatiquement des informations ciblées d’un site web. Dans cette optique, vous avez les specifications suivantes : 

### Choisir un site web avec des données

#### Site Web :

* RS components International : https://fr.rs-online.com/web/c/raspberry-pi-arduino-outils-de-developpement/boutique-raspberry-pi/raspberry-pi/

Ce site est choisi pour chercher la mise à jour des prix du raspberry pi en scrapper les prix et mettre à jour un tableau.

### Choisir un outil de scrapping (bs4, selenium, scrappy… ) :

#### Tool choisi est " Selenium " :

* Pour ses plusieurs utilisations et fonctions , comme click boutons , page scroll.

- Préciser (sous forme de commentaire) la methode de récupération des données 
- Inclure des temps de pauses pour pouvoir suspendre votre code (pendant une seconde par exemple). Cela va vous aider à ne pas être signalé comme spam auprès du site.
- Votre projet dispose d’une documentation claire et concise qui explique les différentes lignes de code ainsi que des commentaire. 
- Présenter votre code sous forme de notebook jupyter en detaillant chaque étapes 
- Dans la mesure du possible, faire une analyse de vos données récupérées
- Paqueter votre script dans un container docker et expliciter les commandes afin de le lancer 
- Refactorer votre code Jupyter en un script python orienté objet en utilisant le module argparse afin de permettre l’utilisation d’input utilisateur dans le lancement du script 