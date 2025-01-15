"""le petit tipe 2.0"""


import random as rd

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

def is_fois(l,x):
  a=0
  for i in range (len(l)):
    if l[i]==x:
      a=a+1
  return a

def point(i):# attribue a chaque carte son nombred e points dans les règles du blackjack
  if is_in([2,3,4,5,6,7,8,9,10],i)==True:
    return i
  elif i==1:
   return 11
  else:
    return 10

def pointtot(l,x):#nombre de point que le joueur a dans la main
  a=0
  for i in range (len(l)):
    a=a+point(l[i])
  return a

def pair(l):#cette fonction indique si un joueur avec 2 carte a une pair ou non
  a=0
  for i in range (2,13):
    if is_fois(l,i)==0:
      a=a+0
    elif is_fois(l,i)==1:
      a=a+0
    else:
      a=a+1
      
  
  
def tableau (l):# cette fonction renvoie  le tableau correspondant a la main initale d'un joueur
  if is_in(l,1) :
    if is_in(l,10):
      return A
    elif is_in(l,11):
      return A
    elif is_in(l,12):
      return A
    elif is_in(l,13):
      return A
    elif is_fois(l,1)==2:
      return Pair
    else :
      return AS
  elif pair(l)>=1:
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
  return a 

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
    return (l,g)


def distribuer(k,n):#ditribue les carte que chaque joueur aura en debut de partie avec n paquet de cartes
  J=jeudecarte(n)
  a=[]
  for i in range (k+1):
    a.append([])
  for i in range (k+1):
    piocher(a[i],J)
  return(a,J)
  
def position(l,k,t):# cette fonction suit la fonction tableau, une fois que le k-ieme joueur se voit attribuer un tableau, cette fonction lui attribue une case dans ce tableau qui va lui dire quoi jouer
#l: la liste des cartes distribuer, k: le k-ieme joueur(ses cartes),t:le tableau qu'il c'est vu attribuer
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



    




