import numpy as np
import matplotlib.pyplot as plt
from copy import*
global rubicube,L
rubicube = np.zeros((5,5,5),dtype=str)
for k in range(1,4):
    for i in range(1,4):
        for j in range(1,4):
            rubicube[k,i,j] = "centre"
for i in range(1,4):
    for j in range(1,4):
        rubicube[0,i,j] = "white"	#derriere
        rubicube[4,i,j] = "blue"  #devant
        rubicube[i,0,j] = "green"  #dessus
        rubicube[i,4,j] = "yellow" #dessous
        rubicube[i,j,0] = "red"	#gauche
        rubicube[i,j,4] = "morange" #droite

def afficher(cube):
    #créer les contours du cube
    A = [1/3,3+1/3,3+1/3,3+2/3,3+2/3,2/3]
    B = [3+1/3,3+1/3,1/3,2/3,3+2/3,3+2/3]
    ax.plot(A,B,'b')

    C = [0,3,4,4,3,0]
    D = [1,1,2,3,2,2]
    ax.plot(C,D,'b')

    R = [1,1,2,3,2,2]
    T = [0,3,4,4,3,0]
    ax.plot(R,T,'b')

    X = [3,3,0,0,3]
    Y = [0,3,3,0,0]
    ax.plot(X,Y,'k')
    U = [0,1,4,3,3,4,4]
    V = [3,4,4,3,0,1,4]
    ax.plot(U,V,'k')

    list_centres_down = [(1/2,1/2),(3/2,1/2),(5/2,1/2),(1/2,3/2),(3/2,3/2),(5/2,3/2),(1/2,5/2),(3/2,5/2),(5/2,5/2)]
    list_centres_up = [(4/6,3+1/6),(1,7/2),(8/6,3+5/6),(1+4/6,3+1/6),(2,7/2),(1+8/6,3+5/6),(2+4/6,3+1/6),(3,7/2),(2+8/6,3+5/6)]
    list_centres_side = [(3+1/6,4/6),(7/2,1),(3+5/6,8/6),(3+1/6,4/6+1),(7/2,2),(3+5/6,8/6+1),(3+1/6,4/6+2),(7/2,3),(3+5/6,8/6+2)]

    k = 0
    l1 = [[]]
    l2 = [[]]
    l3 = [[]]
    for i in range(1,4):
        for j in range(1,4):
            l1[i][j], = ax.plot(list_centres_down[k][0],list_centres_down[k][1],"o"+cube[4,i,j])
            l2[i][j], = ax.plot(list_centres_up[k][0],list_centres_up[k][1],"o"+cube[i,0,j])
            l3[i][j], = ax.plot(list_centres_side[k][0],list_centres_side[k][1],"o"+cube[i,j,4])
            k+=1
    return [l1,l2,l3]
    #afficher les couleurs des cubes

    """liste_rouge_X = [x[0] for x in list_centres_side]
    liste_rouge_Y = []
    plt.plot(l    switch (k%2) {
iste_rouge_X,liste_rouge_Y,'or')

    liste_vert_X = []
    liste_vert_Y = []
    plt.plot(liste_vert_X,liste_vert_Y,'og')

    liste_jaune_X = [x[0] for x in list_centres_side]
    liste_jaune_Y = [x[1] for x in list_centres_side]
    plt.plot(liste_jaune_X,liste_jaune_Y,'oy')

    liste_bleu_X = [x[0] for x in list_centres_down]
    liste_bleu_Y = [x[1] for x in list_centres_down]
    plt.plot(liste_bleu_X,liste_bleu_Y,'ob')

    liste_blanc_X = [x[0] for x in list_centres_up]
    liste_blanc_Y = [x[1] for x in list_centres_up]
    plt.plot(liste_blanc_X,liste_blanc_Y,'ok')

    liste_orange_X = [x[0] for x in list_centres_side]
    liste_orange_Y = [x[1] for x in list_centres_side]
    plt.plot(liste_orange_X,liste_orange_Y,'o(127,60,60)')
"""


def tourner_cote(cube,sens):
    face_cote = [copy(cube[0,1:4,1:4]),copy(cube[1:4,1:4,0]),copy(cube[4,1:4,1:4]),copy(cube[1:4,1:4,4])]
    #[derriere,gauche,devant,droite]
    if sens == True:
        cube[0,1:4,1:4] = face_cote[1]
        cube[1:4,1:4,0] = face_cote[2]
        cube[4,1:4,1:4] = face_cote[3]
        cube[1:4,1:4,4] = face_cote[0]
    else:
        cube[0,1:4,1:4] = face_cote[3]
        cube[1:4,1:4,0] = face_cote[0]
        cube[4,1:4,1:4] = face_cote[1]
        cube[1:4,1:4,4] = face_cote[2]
    return cube

def tourner_haut(cube,sens):
    face_cote = [cube[0,1:4,1:4].copy(),cube[1:4,0,1:4].copy(),cube[4,1:4,1:4].copy(),cube[1:4,4,1:4].copy()]
    #[derriere,dessus,devant,dessous]
    if sens == True:
        cube[0,1:4,1:4] = face_cote[1]
        cube[1:4,1:4,0] = face_cote[2]
        cube[4,1:4,1:4] = face_cote[3]
        cube[1:4,1:4,4] = face_cote[0]
    else:
        cube[0,1:4,1:4] = face_cote[3]
        cube[1:4,1:4,0] = face_cote[0]
        cube[4,1:4,1:4] = face_cote[1]
        cube[1:4,1:4,4] = face_cote[2]

def onclick(event):
    print("click")
    #print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
    #      ('double' if event.dblclick else 'single', event.button,
    #       event.x, event.y, event.xdata, event.ydata))

print(rubicube)
fig = plt.figure()
ax = fig.add_subplot(111)
L = afficher(rubicube)

def onkey(event):
    print("la touche appuyée est %s"%(event.key))
    global rubicube,L
    #print(type(rubicube),L)
    commande = event.key
    print(rubicube)
    if commande == "up":
        tourner_haut(rubicube,True)

    elif commande == "down":
        tourner_haut(rubicube,False)
    elif commande == "left":
        tourner_cote(rubicube,True)
    elif commande == "right":
        tourner_cote(rubicube,False)
    print("__________________________________________\n",rubicube)
    for i in range(1,4):
        for j in range(1,4):
            #print(rubicube[4,i,j])
            L[0][i][j].set_color(rubicube[4,i,j])
            L[1][i][j].set_color(rubicube[i,0,j])
            L[2][i][j].set_color(rubicube[i,j,4])
            L[0][i][j].figure.canvas.draw()
            L[1][i][j].figure.canvas.draw()
            L[2][i][j].figure.canvas.draw()


cid = fig.canvas.mpl_connect('key_press_event',onkey)
cid = fig.canvas.mpl_connect('button_press_event',onclick)
plt.show()
