from math import e
from math import sin
from math import sqrt
from random import uniform
from operator import add

#Funcion de evaluacion
def func(x, part):
  res = (x / part[0]) + (part[1] * e**(part[2] / x)) + part[3] * sin(x)
  return round(res,6)
#Funcion que retorna la sumatoria de la funcion evaluada para cierta particula
def evalPart(part, exp):
  res = 0
  for item in exp:
    res += (exp[item] - func(item, part))**2
  #print(res)
  return res/len(exp)

def check(part):
  auxPart = part
  for i, item in enumerate(part):
    if item > 15:
      auxPart[i] = 15
    elif item < 1:
      auxPart[i] = 1
    else:
      auxPart[i] = round(item,6)
  return auxPart

#Funcion que calcula y retorna la velocidad de una particula
def calcVel(part, exp, g, mejorx, alpha, beta, vel):
  finalvel = [0,0,0,0]
  for i, part in enumerate(part):
    finalvel[i] += vel[i]
    finalvel[i] += (beta*round(uniform(0, 1), 6)*(mejorx[i]-part))
    finalvel[i] += (alpha*round(uniform(0, 1), 6)*(g[i]-part))
    
    finalvel[i] = round(finalvel[i],6)
  return finalvel
#Funcion que regresa la magnitud de un vector
def magnitud(vel):
  mag = 0
  for i in vel:
    mag += i**2
  return round(sqrt(mag),6)
#Funcion que ajusta el vector de velocidad
def newVel(vel,max):
  mag = magnitud(vel)
  auxvel = vel
  for i, item in enumerate(vel):
    auxvel[i] = round((item/mag)*max,6)
  return auxvel

#Valores esperados
exp = {2: 26, 4: -1, 6: 4, 8: 20, 10: 0, 12: -2, 14: 19, 16: 1, 18: -4, 20: 19}

t = 0  #Variable que representa el numero de iteraciones
sumExp = 0  #Variable con la sumatoria de los esperado
alpha = 2   #Constante de aceleracion 1
beta = 2    #Constante de aceleracion 2
g = [15,15,15,15]   #Mejor global dummy
maxVel = 8  #Constante de valocidad maxima
#Calculo de mejor global
for item in exp:
  sumExp += exp[item]
#Inicializacion de 5 particulas con 4 valores entre 1-15
particulas = [[round(uniform(1, 15), 6) for i in range(4)] for j in range(5)]
#Inicializacion de mejor local
mejorx = [[0 for i in range(4)]for j in range(5)]

for i, part in enumerate(particulas):
  mejorx[i] = part

#Inicializacion de velocidad de particulas
vel = [[0 for i in range(4)] for j in range(5)]
#optener mejor global
for part in particulas:
  if evalPart(part, exp) < evalPart(g, exp):
    g = part

while t < 20:
  for i, part in enumerate(particulas):
    #Calcular velocidad
    vel[i] = calcVel(part, exp, g, mejorx[i], alpha, beta, vel[i])
    if magnitud(vel[i]) > maxVel:
      vel[i] = newVel(vel[i],maxVel)
    #Nueva posicion
    particulas[i] = list(map(add, part,vel[i]))
    particulas[i] = check(particulas[i])
    #Encontar mejor local
    if evalPart(particulas[i], exp) < evalPart(mejorx[i], exp):
      mejorx[i] = part
  #Encontrar mejor global
  for part in particulas:
    if evalPart(part, exp) < evalPart(g, exp):
      g = part
  t += 1

#Impresion de resultados
print('Mejor: ', g)
print('Error:', evalPart(g, exp))
#print(sumExp)
#print(list(func(i, g) for i in exp))