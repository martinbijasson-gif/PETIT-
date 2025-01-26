"""le petit tipe 2.0"""

#THP: Commentaire globale: c'est horriblement mal codé et je ne peux que le dire aussi crûment que cela !! Dans tous les cas, il faut qu'on en parle ! J'ai refait des choses, mais de toute façon je ne peux même pas deviner ce qu'il faut faire avec tout ça...

import random as rd

#THP: Ca aurait été bien de dire à quoi correspondent s,h,d,p

A=[["s","s","s","s","s","s","s","s","s","s"],#21,20,19,18,17#ce tableau etablie une strategie de jeu si le joueur n'as pas d'as,ni de pair chaqueligne correspond a la somme despoint des carte du joueur 
   ["s","s","s","s","s","h","h","h","h","s"],#16
   ["s","s","s","s","s","h","h","h","s","s"],#15
   ["s","s","s","s","s","h","h","h","h","h"],#14
   ["h","h","s","s","s","h","h","h","h","h"],#13
   ["d","d","d","d","d","d","d","d","d","h"],#12
   ["d","d","d","d","d","d","d","d","h","h"],#11
   ["h","d","d","d","d","h","h","h","h","h"],#10
   ["h","h","h","h","h","h","h","h","h","h"]]#<=9

AS=[["s","s","s","s","s","s","s","s","s","s",],#10  #stratégie de jeu lorsque le joueur a un seul as dans son jeu
    ["s","d","d","d","d","s","s","h","h","h",],#9
    ["h","d","d","d","d","h","h","h","h","h",],#8
    ["h","h","d","d","d","h","h","h","h","h",],#7
    ["h","h","h","d","d","h","h","h","h","h",],]#<=6

Pair=[["p","p","p","p","p","p","p","p","p","p",],#1  #strategie de jeu lorsque le joueur a une pair dans son jeu
      ["s","s","s","s","s","s","s","s","s","s",],#10
      ["p","p","p","p","p","s","p","p","s","s",],#9
      ["p","p","p","p","p","p","p","p","p","p",],#8
      ["p","p","p","p","p","p","h","h","h","h",],#7
      ["p","p","p","p","p","h","h","h","h","h",],#6
      ["d","d","d","d","d","d","d","d","h","h",],#5
      ["h","h","h","p","p","h","h","h","h","h",],#4
      ["p","p","p","p","p","p","h","h","h","h",],#3
      ["p","p","p","p","p","p","h","h","h","h",]]#2

def is_in(l,x):
  for i in range (len(l)):
    if l[i]==x:
      return True  
  return False

def is_in_THP(l,x):
  return l.count(x)!=0

def is_fois(l,x):
  a=0
  for i in range (len(l)):
    if l[i]==x:
      a=a+1
  return a

def is_fois_THP(l,x):
  return l.count(x)

def point_THP(i):# attribue a chaque carte son nombre de points dans les règles du blackjack
  if 2<=i<=10: 
    return i
  elif i==1:
   return 11
  else:
    return 10

def point(i):# attribue a chaque carte son nombred e points dans les règles du blackjack
  if is_in([2,3,4,5,6,7,8,9,10],i)==True: #THP: if 2<=i<=10 
    return i
  elif i==1:
   return 11 #THP: Je pensais qu'on pouvait choisir entre 1 et 11 ?
  else:
    return 10

def pointtot_THP(l):
  return sum(list(map(point_THP,l)))

def pointtot(l,x):#nombre de point que le joueur a dans la main #THP: C'est quoi x ??
  a=0
  for i in range (len(l)):
    a=a+point(l[i])
  return a

def pair(l):#cette fonction indique si un joueur avec 2 carte a une pair ou non 
  #THP: Tu ne vérifies pas si le joueur a 2 cartes ? Si c'est le cas, cette fonction est triviale !! (return l[1]==l[2])
  a=0
  for i in range (2,13): #THP: On exclut les pairs d'as et de rois ? (Je ne sais pas, je ne connais pas les stratégies du blackjack)
    if is_fois(l,i)==0:
      a=a+0
    elif is_fois(l,i)==1:
      a=a+0
    else:
      a=a+1
  #THP: Cette fonction ne renvoie rien. Par ailleurs, le commentaire que tu donnes indique qu'elle devrait renvoyer un booléen, or la seule variable que tu construis est un entier.
      
def paire_THP(l):
  return max([l.count(x)==2 for x in range(2,13)])
  
def tableau(l):# cette fonction renvoie  le tableau correspondant a la main initale d'un joueur
  if is_in(l,1) :
    if is_in(l,10):
      return A
    elif is_in(l,11): #THP: Pourquoi ne pas juste mettre un or ??
      return A
    elif is_in(l,12):
      return A
    elif is_in(l,13):
      return A
    elif is_fois(l,1)==2:
      return Pair
    else :
      return AS
  elif pair(l)>=1: # THP: Oui, donc en fait, on regarde bien s'il y a une paire ou non, donc c'est bien un booléen qu'il nous fallait renvoyer...
    return Pair
  else:
    return A

def tableau_THP(l):
  if 1 in l:
    if 10 in l or 11 in l or 13 in l:
      return A
    elif is_fois_THP(l,1)==2: #THP: J'ai réutilisé la fonction is_in_THP du début mais c'est ridicule, l.count(1)==2 aurait été plus clair et plus efficace...
      return Pair
    else:
      return AS
  elif paire_THP(l):
    return Pair
  else:
    return A

def jeudecarte(n):#crée un jeu de carte initiale avec n paquet dans lequel l'on va piocher pendant la partie
  a=[]
  b=[]
  for i in range (1,14):
    b.append(i)
  for i in range (4*n):
    a.append(b)
  return a #THP: Pourquoi la liste finale n'est pas aplatie ?

def piocher(l,g):#cette fonction doit prendre une carte dans les jeu de carte (g) pour la mettre dans (l) de plus cette carte ne pourra jamais etre reprise dans g
    c=len(l)
    while len(l)==c:
        a=rd.randint(0,len(g))
        b=rd.randint(0,len(g[1]))
        if g[a][b]==0:
            l==l
        else:
            l.append(g[a][b])
            g[a][b]=0
    return (l,g) #Tu pars du principe qu'il n'y a qu'un joueur ? Autrement tu ne pourras jamais décrire une partie consistante avec ça !


def distribuer(k,n):#ditribue les carte que chaque joueur aura en debut de partie avec n paquet de cartes
  J=jeudecarte(n)
  a=[]
  for i in range (k+1):
    a.append([])
  for i in range (k+1):
    piocher(a[i],J)
  return(a,J) #THp: Et c'est quoi a ici ? Comment on peut avoir quelque chose de logiquement consistant avec ce qui précède ???
  
def position(l,k,t):# cette fonction suit la fonction tableau, une fois que le k-ieme joueur se voit attribuer un tableau, cette fonction lui attribue une case dans ce tableau qui va lui dire quoi jouer
#l: la liste des cartes distribuer, k: le k-ieme joueur(ses cartes),t:le tableau qu'il c'est vu attribuer
  #THP: Au-delà de la grammaire catastrophique de la phrase qui précède, je ne comprends rien. l est une liste ? une liste de listes ? quel rapport avec ce qui précède ?
  if l[n][0]<=10:
    n=l[n][0]-1
  else: n=9
  if t==A:
    a=0
    for i in range (len(l[k])):
      a=a+l[k][i]
    if a>=17:
      return A[0][n]
    elif a<=9:
      return A[8][n]
    else:
      return A[17-a][n]
  elif t==AS:
    a=l[k][1]
    #il faut que je retrie mes carte quand j'ai un as et que je mette la carte qui n'en est pas un en deuxieme position
    #THP: Que dois-je dire d'autre que "ok" ? Qu'est-ce que ça fait là, cette phrase ne veut rien dire en français de toute façon, et même si j'extrapole je ne vois pas bien dans quel monde on doit trier sa main au blackjack ?
    if a>=6:
      return AS[10-a][n]
    else:
      return AS[4][n]
  else:
    if l[k][0]==1:
      return Pair[0][n]
    else:
      return Pair[11-l[k][0]]
    
def partie(k,n,p,m):#joue une partie avec k joueur , n paquets, p manches et m la mise
  a=distribuer (k,n)[0]
  #THP: Parce qu'une partie se résume à une distribution initiale ?


    




