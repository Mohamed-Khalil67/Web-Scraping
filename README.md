# Web-Scraping

## Objectif du projet : Pour un client (fictif ou non) vous devez coder un script python qui permet d’extraire automatiquement des informations ciblées d’un site web. Dans cette optique, vous avez les specifications suivantes : 

### Choisir un site web avec des données

#### Site Web :

* Amazon.fr : https://www.amazon.fr/

Ce site est choisi pour chercher la mise à jour des prix du raspberry pi en scrapper les prix et mettre à jour un tableau.

### Choisir un outil de scrapping (bs4, selenium, scrappy… ) :

#### Tool choisi est " Selenium " :

* Pour ses plusieurs utilisations et fonctions , comme click boutons , page scroll.
* Possibilitées d'aller sur plusieurs pages et récupérer les données

#### La méthode selenium pour récupération des données

* On va afficher tous les produits qui concerne le 'raspberry pi 4' sur amazon afin de visualiser les prix et leurs changements
* il y a une manipulation et enregistrement des données à partir des class balises sur les pages amazon html qui concerne les prix , name , asin , rating ,rating_num et liens pour ces produits
* Aprés , ils sont enregistrées dans des listes qui itérent dans la page html en utilisant les méthodes find.element ou elements 
* Energistrement des données dans un fichier amazon_search.db afin de le récupérer aprés et le présenter en format tableau en utilisant script python flask.

#### Temps de suspensation:

* les temps des suspensions est ajoutée aprés chaque ouverture d'une page aprés et avant clickant au dessus en utilisant : driver.implicitly_wait(5)

#### Clean code :

* clean code est fait en commencant avec les essais de jupyter notebook , ( ipynb ) , pour essayer chaque partie du code et scrapping en générale

* Mes données comme expliquées sont les infos prix et compositions et liens du produit : rapsberry pi 4 , le produit m'a interessé puisque les prix sont trop augmenté pour les circuits embarquées

#### Container creation :

* Deux containeur sont censées d'être crées et avoir une connection network entre eux mais par rapport au recherche j'ai réalisé que c'est pas implémenté jusqu'à maintenant.
* J'ai réussie à lancer selenium standalone chrome et lancer mon script python dépendant du ce container.


#### Refactoration du code en jupyter :

* The app.py script est codé sous forme des fonctions qui se lance l'un aprés l'autre , scrape_amazon(). en choissisant les nombres de pages à scrapper et le keyword du produit.