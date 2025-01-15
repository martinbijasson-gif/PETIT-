import random

LE CODE SI DESSOUS SIMULE UNE PARTIE DE BLACKJACK MAIS LES CARTES DEJA PIOCHER NE SONT PAS RETIRER DU PAQUET


def is_in(l,x):
  for i in range (len(l)):
    if l[i]==x:
      return True  
  return False

def distribue(n):
  a=[]
  for i in range(n+1):
    b=[]
    c=random.randint(1,13)
    d=random.randint(1,13)
    b.append([c,d])
    a.append(b)
  return a
                        

def point(i):
  if is_in([2,3,4,5,6,7,8,9,10],i)==True:
    return i
  elif i==1:
   return 11
  else:
    return 1
  
    

def jouer(l):
  a=0
  for i in range(len(l)):
    a==a+point(l[i])
  if a==21:
    return "blackjack"
  while a<=14:
    a =a+point(random.randint(1,13))
  return a

def dealer(l):
  a=0
  for i in range(len(l)):
    a=a+point(l[i])
  while a<=17:
    a=a+(point(random.randint(1,13)))
  return a

def partie(a,b,c):
  #a:le nombre de joueurs,b:le nombre de manche,c:la mise a chaque manche
  e=[]
  for i in range(a):
    e.append(0)#on crée une liste qui va donner les gains de chaque joueur
  for i in range(b):
    d=distribue(a)
    l=[]
    for j in range(a):
      l.append(jouer(d[i]))
    l.append(dealer(d[i]))
    for j in range(len(l)):
      if l[j]=="blackjack":
        e[j]=e[j]+(1.5)*c
      else:
        if l[j]<=l[a+1]:
          e[j]=e[j]-c
        elif l[j]>=22:
          e[j]=e[j]-c
        else:
          e[j]=e[j]+c
 return e   
        