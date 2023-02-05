# Q-Learning

The purpose of this exercice is to create an AI dedicated to Dungeon Maps generation.
From a 4x4 matrice, the AI will generate a matrice with a starting point, an ending point and
a treasure point. Each cell will contain 0 to 4 walls, 0 to 1 starting keypoint, 0 to 1 treasure
keypoint and 0 to 1 ending keypoint. A cell can contain only 1 keypoint.


Approach Developped :
Our approach consist to generate a a 4*4 matrix and to process a key perfomance indicator ( KPI ) wich indicates the difficulty of our grid.
https://fr.wikipedia.org/wiki/Matrice_d%27adjacence

To process KPI of difficulty : we transform our 4*4 matrix in an adjacence matrix with size 16*16.
It s an adpation of Dijkstra : https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra


We generated a follwing grid :

![map](https://user-images.githubusercontent.com/124429102/216813343-4beb955a-9343-4a27-b54a-c435d04b235f.png)


We process all possibility of different size of path :

![maze](https://user-images.githubusercontent.com/124429102/216813366-33f6d251-fc5d-47ff-ad3f-b41707df553d.png)


To run this script :
python 3.11
Pip install numpy
