from math import e
from math import sin
from random import uniform
from operator import add

#Funcion de evaluacion
def func(x, part):
  res = (x / part[0]) + (part[1] * e**(part[2] / x)) + part[3] * sin(x)
  return res
#Funcion que retorna la sumatoria de la funcion evaluada para cierta particula
def evalPart(part, exp):
  res = 0
  for item in exp:
    res += func(item, part)
  return res
#Funcion que calcula y retorna la velocidad de una particula
def calcVel(part, exp, g, mejorx, alpha, beta, vel):
  finalvel = [0,0,0,0]
  for i, part in enumerate(part):
    finalvel[i] += vel[i]
    finalvel[i] += (alpha*round(uniform(0, 1), 2)*(g[i]-part))
    finalvel[i] += (beta*round(uniform(0, 1), 2)*(mejorx[i]-part))
    finalvel[i] = round(finalvel[i],2)
  return finalvel


#Valores esperados
exp = {2: 26, 4: -1, 6: 4, 8: 20, 10: 0, 12: -2, 14: 19, 16: 1, 18: -4, 20: 19}

t = 0  #Variable que representa el numero de iteraciones
sumExp = 0  #Variable con la sumatoria de los esperado
alpha = 2   #Constante de aceleracion 1
beta = 2    #Constante de aceleracion 2
g = [15,15,15,15]   #Mejor global dummy
#Calculo de mejor global
for item in exp:
  sumExp += exp[item]
#Inicializacion de 5 particulas con 4 valores entre 1-15
particulas = [[round(uniform(1, 15), 2) for i in range(4)] for j in range(5)]
#Inicializacion de mejor local
mejorx = particulas
#Inicializacion de velocidad de particulas
vel = [[0 for i in range(4)] for j in range(5)]
#optener mejor global
for part in particulas:
  if abs(evalPart(part, exp) - sumExp) < abs(evalPart(g, exp) - sumExp):
    g = part

while t < 10:
  for i, part in enumerate(particulas):
    #Calcular velocidad
    vel[i] = calcVel(part, exp, g, mejorx[i], alpha, beta, vel[i])
    #Nueva posicion
    particulas[i] = list(map(add, part,vel[i]))
    #Encontar mejor local
    if abs(evalPart(part, exp) - sumExp) < abs(evalPart(mejorx[i], exp) - sumExp):
      mejorx[i] = part
  #Encontrar mejor global
  for part in particulas:
    if abs(evalPart(part, exp) - sumExp) < abs(evalPart(g, exp) - sumExp):
      g = part
  t += 1
#Impresion de resultados
print(g)
print(evalPart(g, exp))
print(sumExp)