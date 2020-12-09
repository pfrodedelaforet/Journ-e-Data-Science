Question 1 : est-ce que les arbitres de football sont plus enclins à donner un carton (rouge) à des joueurs 
à la peau foncée qu'à ceux à la peau claire?

Question 2 : est-ce que les arbitres originaires d'un pays caractérisé par un fort préjudice envers 
la couleur de peau sont plus enclins à donner un carton rouge aux joueurs de couleur?

________________________________________________________________________________________________________________

Les données proviennent d'une société spécialisée dans les statistiques sportives. Elles comprennent des informations sur
des joueurs de football (N= 2053), ayant participé aux championnats d'Angleterre, d'Allemagne, de France et d'Espagne durant la saison 
2012-2013, ainsi que des informations sur les arbitres (N = 3147) que ces joueurs ont rencontré au cours de leur carrière professionnelle
jusqu'à la saison 2012. 

Un jeu de données de dyades joueur/arbitre inclut le nombre de matchs au cours desquels un joueur et un arbitre ce sont recontrés, ainsi que le 
nombre total de cartons rouges que le joueur a reçu de l'arbitre durant leurs rencontres. 

Les photos de 1586 des 2053 joueurs étaient disponibles. La couleur de peau du joueur a été scorée par deux scoreurs indépendants qui ignoraient la 
question de recherche. Le score est un entier entre 1 (très claire) et 5 (très foncée). 

De plus, un score de biais culturel implicite a été calculé pour chaque arbitre, à l'aide d'un test "d'association raciale implicite", les hautes valeurs
correspondant à une forte inclination à des associations blanc-bon, noir-mauvais. Un score explicite de biais a également été déterminé pour 
chaque arbitre, à l'aide d'un "thermomètre racial", les hautes valeurs correspondant à un sentiment chaleureux envers les blancs plutôt que les noirs.
Ces deux scores ont été crés par aggrégation de résultats de tests passés par un nombre important d'internautes dans les pays respectifs des arbitres.

En tout, le jeu de données comprend 146028 dyades joueurs/arbitres. 

Description des variables :
 
playerShort : 
ID du joueur

player :
nom du joueur

club :
club du joueur

leagueCountry :
pays du club du joueur (Angleterre, Allemagne, France, Espagne)

birthday
date anniversaire du joueur

height
taille du joueur en cm

weight
poids du joueur en kg

position
position du joueur dans le jeu

games
nombre de matchs dans la dyade joueur/arbitre

victories
nombre de victoires dans la dyades joueur/arbitre

ties
nombre de matchs nuls dans la dyade joueur/arbitre

defeats
nombres de défaites dans la dyade joueur/arbitre

goals
nombre de buts marqués par le joueur dans la dyade joueur/arbitre

yellowCards
nombre de cartons jaunes reçus de l'arbitre

yellowReds
nombre de cartons jaunes et rouges reçus de l'arbitre (lorsqu'au cours du match le joueur a reçu 2 jaunes)

redCards
nombre de cartons rouges reçus de l'arbitre

photoID
ID de la photo du joueur (si disponible)

rater1
score sur une échelle de 5 valeurs de la couleur de peau du joueur par le premier scoreur (0: très claire, 1: très foncée)

rater2
score sur une échelle de 5 valeurs de la couleur de peau du joueur par le second scoreur (0: très claire, 1: très foncée)

refNum
ID unique de l'arbitre

refCountry
ID unique du pays

Alpha_3
Indicatif du pays

meanIAT
Score moyen de biais culturel implicite pour un arbitre donné (haute valeur : association usuelle blanc - bon, noir-mauvais)

nIAT
Taille de l'échantillon d'internautes pour déterminer le score de biais culturel implicite pour tel pays.

seIAT
écart type du score de biais culturel implicite.

meanExp
Score moyen de biais racial explicite (obtenu par thermomètre racial) pour tel pays (haute valeur = plus fort sentiments positifs envers les blancs
que les noirs)

nExp
Taille de l'échantillon pour le calcul du score de biais explicite.

seExp
écart type du score de biais racial explicite.